#!/usr/bin/env python3
"""
extract-page-structure.py
Parses HTML and extracts structural data for competitor landing page analysis.

Usage:
    python3 extract-page-structure.py <html_file>
    echo "<html>...</html>" | python3 extract-page-structure.py --stdin

Output: JSON with headings, forms, buttons, word count, section count, framework detection.
"""

import sys
import json
import re
from html.parser import HTMLParser


class PageStructureExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.headings = []
        self.forms = []
        self.buttons = []
        self.images = []
        self.scripts = []
        self.meta_tags = []
        self.links = []

        # State tracking
        self._current_tag = None
        self._current_attrs = {}
        self._current_text = ""
        self._in_form = False
        self._current_form = {"fields": [], "action": None, "method": None}
        self._tag_stack = []
        self._section_markers = 0
        self._all_text = []
        self._skip_tags = {"script", "style", "noscript"}
        self._skip_depth = 0

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        self._tag_stack.append(tag)

        # Skip content inside script/style
        if tag in self._skip_tags:
            self._skip_depth += 1
            # Still collect script src for framework detection
            if tag == "script":
                self.scripts.append(attrs_dict.get("src", "[inline]"))
            return

        if self._skip_depth > 0:
            return

        # Headings
        if tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
            self._current_tag = tag
            self._current_text = ""

        # Buttons
        elif tag == "button":
            self._current_tag = "button"
            self._current_text = ""

        # Input with type=submit (also a CTA)
        elif tag == "input" and attrs_dict.get("type") == "submit":
            self.buttons.append({
                "type": "input-submit",
                "text": attrs_dict.get("value", ""),
            })

        # Links that look like CTAs
        elif tag == "a":
            self._current_tag = "a"
            self._current_text = ""
            self._current_attrs = attrs_dict

        # Forms
        elif tag == "form":
            self._in_form = True
            self._current_form = {
                "action": attrs_dict.get("action", ""),
                "method": attrs_dict.get("method", "GET").upper(),
                "fields": [],
            }

        # Form fields
        elif self._in_form and tag in ("input", "select", "textarea"):
            input_type = attrs_dict.get("type", "text")
            if input_type not in ("hidden", "submit"):
                self._current_form["fields"].append({
                    "tag": tag,
                    "type": input_type,
                    "name": attrs_dict.get("name", ""),
                    "required": "required" in attrs_dict,
                    "placeholder": attrs_dict.get("placeholder", ""),
                })

        # Images
        elif tag == "img":
            self.images.append({
                "src": attrs_dict.get("src", ""),
                "alt": attrs_dict.get("alt", ""),
                "loading": attrs_dict.get("loading", "eager"),
                "has_alt": bool(attrs_dict.get("alt", "").strip()),
            })

        # Meta tags
        elif tag == "meta":
            self.meta_tags.append(attrs_dict)

        # Section markers
        elif tag in ("section", "article"):
            self._section_markers += 1

        # Link tags (for font detection)
        elif tag == "link":
            self.links.append(attrs_dict)

    def handle_endtag(self, tag):
        if tag in self._skip_tags and self._skip_depth > 0:
            self._skip_depth -= 1
            return

        if self._skip_depth > 0:
            return

        if self._tag_stack and self._tag_stack[-1] == tag:
            self._tag_stack.pop()

        # Capture heading text
        if tag in ("h1", "h2", "h3", "h4", "h5", "h6") and self._current_tag == tag:
            text = self._current_text.strip()
            if text:
                self.headings.append({
                    "level": tag,
                    "text": text,
                })
            self._current_tag = None

        # Capture button text
        elif tag == "button" and self._current_tag == "button":
            text = self._current_text.strip()
            if text:
                self.buttons.append({
                    "type": "button",
                    "text": text,
                })
            self._current_tag = None

        # Capture link text (CTA candidates)
        elif tag == "a" and self._current_tag == "a":
            text = self._current_text.strip()
            href = self._current_attrs.get("href", "")
            classes = self._current_attrs.get("class", "")
            # Keep links that look like CTAs (have button-like classes or short text)
            is_cta = any(kw in classes.lower() for kw in ("btn", "button", "cta")) or (
                text and len(text) < 40 and href and not href.startswith("#")
            )
            if text and is_cta:
                self.buttons.append({
                    "type": "link-cta",
                    "text": text,
                    "href": href,
                })
            self._current_tag = None

        # Close form
        elif tag == "form" and self._in_form:
            self.forms.append(self._current_form)
            self._in_form = False

    def handle_data(self, data):
        if self._skip_depth > 0:
            return

        if self._current_tag:
            self._current_text += data

        # Collect all visible text for word count
        self._all_text.append(data)

    def get_word_count(self):
        full_text = " ".join(self._all_text)
        words = re.findall(r"\b\w+\b", full_text)
        return len(words)

    def get_section_count(self):
        # Use explicit section/article tags if present, otherwise estimate from h2 count
        if self._section_markers > 0:
            return self._section_markers
        h2_count = sum(1 for h in self.headings if h["level"] == "h2")
        return max(h2_count, 1)

    def detect_framework(self):
        all_scripts = " ".join(self.scripts)
        all_meta = json.dumps(self.meta_tags)

        checks = [
            ("Next.js", ["_next/", "__NEXT_DATA__", "__next"]),
            ("React", ["react", "react-dom", "ReactDOM"]),
            ("Vue.js/Nuxt", ["__nuxt", "_nuxt/", "data-v-", "vue"]),
            ("WordPress", ["wp-content", "wp-includes", "wordpress"]),
            ("Wix", ["wix.com", "_wixCIDX", "wixsite"]),
            ("Squarespace", ["squarespace.com", "sqs-block"]),
            ("Shopify", ["cdn.shopify.com", "Shopify.theme"]),
            ("Webflow", ["webflow.com", "w-embed"]),
        ]

        detected = []
        source = all_scripts + " " + all_meta
        for name, signals in checks:
            if any(sig.lower() in source.lower() for sig in signals):
                detected.append(name)

        return detected if detected else ["Static HTML / Unknown"]

    def detect_analytics(self):
        all_scripts = " ".join(self.scripts)
        analytics = []

        checks = [
            ("Google Tag Manager", ["googletagmanager.com", "gtm.js"]),
            ("Google Analytics", ["google-analytics.com", "gtag/js", "ga.js"]),
            ("Facebook Pixel", ["connect.facebook.net", "fbevents.js", "fbq("]),
            ("Hotjar", ["hotjar.com", "hj("]),
            ("TikTok Pixel", ["analytics.tiktok.com"]),
        ]

        for name, signals in checks:
            if any(sig.lower() in all_scripts.lower() for sig in signals):
                analytics.append(name)

        return analytics

    def has_viewport_meta(self):
        for meta in self.meta_tags:
            if meta.get("name", "").lower() == "viewport":
                return True
        return False

    def get_meta_description(self):
        for meta in self.meta_tags:
            if meta.get("name", "").lower() == "description":
                return meta.get("content", "")
        return None

    def get_page_title(self):
        # Title is not captured by meta — it needs special handling
        # We check headings as proxy; real title would need separate parsing
        return None


def extract(html_content):
    """Parse HTML and return structured JSON."""
    parser = PageStructureExtractor()
    parser.feed(html_content)

    images_with_alt = sum(1 for img in parser.images if img["has_alt"])
    lazy_loaded = sum(1 for img in parser.images if img["loading"] == "lazy")

    result = {
        "headings": parser.headings,
        "forms": parser.forms,
        "buttons": parser.buttons,
        "stats": {
            "word_count": parser.get_word_count(),
            "section_count": parser.get_section_count(),
            "heading_count": len(parser.headings),
            "form_count": len(parser.forms),
            "cta_count": len(parser.buttons),
            "image_count": len(parser.images),
            "images_with_alt": images_with_alt,
            "images_lazy_loaded": lazy_loaded,
            "script_count": len(parser.scripts),
        },
        "tech": {
            "framework": parser.detect_framework(),
            "analytics": parser.detect_analytics(),
            "has_viewport_meta": parser.has_viewport_meta(),
            "meta_description": parser.get_meta_description(),
        },
    }

    return result


def main():
    if "--stdin" in sys.argv:
        html = sys.stdin.read()
    elif len(sys.argv) > 1 and sys.argv[1] != "--stdin":
        filepath = sys.argv[1]
        with open(filepath, "r", encoding="utf-8") as f:
            html = f.read()
    else:
        print("Usage: python3 extract-page-structure.py <html_file>")
        print("       echo '<html>...</html>' | python3 extract-page-structure.py --stdin")
        sys.exit(1)

    result = extract(html)
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
