from django.templatetags.static import static
from django.urls import reverse_lazy, reverse

UNFOLD = {
    "SITE_TITLE": "Admin",
    "SITE_HEADER": "Admin",
    "SITE_SUBHEADER": "FooBar hunter42",
    "SITE_URL": "/",
    "SITE_ICON": {
        "light": lambda request: static("logo-icon.svg"),  # light mode
        "dark": lambda request: static("logo-icon-white.svg"),  # dark mode
    },
    "SITE_SYMBOL": "speed",  # symbol from icon set
    "SHOW_HISTORY": False,  # show/hide "History" button, default: True
    "SHOW_VIEW_ON_SITE": False,  # show/hide "View on site" button, default: True
    "SHOW_BACK_BUTTON": True,  # show/hide "Back" button on changeform in header, default: False
    # "DASHBOARD_CALLBACK": "sample_app.dashboard_callback",
    "BORDER_RADIUS": "8px",
    "COLORS": {
        "base": {
            "50": "243, 244, 246",
            "100": "243, 244, 246",
            "200": "229, 231, 235",
            "300": "209, 213, 219",
            "400": "156, 163, 175",
            "500": "107, 114, 128",
            "600": "75, 85, 99",
            "700": "55, 65, 81",
            "800": "31, 41, 55",
            "900": "17, 24, 39",
            "950": "3, 7, 18",
        },
        "primary": {
            "50": "231, 240, 254",
            "100": "183, 210, 251",
            "200": "135, 180, 249",
            "300": "87, 149, 247",
            "400": "63, 134, 245",
            "500": "39, 119, 244",
            "600": "15, 104, 243",  # RAUSYS Blue
            "700": "12, 83, 194",
            "800": "9, 62, 146",
            "900": "4, 31, 73",
            "950": "1, 10, 24",
        },
        "font": {
            "subtle-light": "var(--color-base-500)",  # text-base-500
            "subtle-dark": "var(--color-base-400)",  # text-base-400
            "default-light": "var(--color-base-600)",  # text-base-600
            "default-dark": "var(--color-base-300)",  # text-base-300
            "important-light": "var(--color-base-900)",  # text-base-900
            "important-dark": "var(--color-base-100)",  # text-base-100
        },
    },
    "SIDEBAR": {
        "show_search": True,  # Search in applications and models names
        "show_all_applications": True,  # Dropdown with all applications and models
        "navigation": [{
                "title": "Navigation",
                "separator": True,
                "collapsible": False,
                "items": [
                    {
                        "title": "Foo",
                        "icon": "group",
                        "link": reverse_lazy("admin:awzm_foo_changelist"),
                        "active": lambda r: reverse('admin:awzm_foo_changelist') in r.path
                    },{
                        "title": "Bar",
                        "icon": "package_2",
                        "link": reverse_lazy("admin:awzm_bar_changelist"),
                        "active": lambda r: reverse('admin:awzm_bar_changelist') in r.path
                    },
                ],
            },
        ],
    },
    "TABS": [{
            "models": [
                "awzm.foo",
                "awzm.bar",
            ],
            "items": [{
                    "title": "Foo",
                    "link": reverse_lazy("admin:awzm_foo_changelist"),
                }, {
                    "title": "Bar",
                    "link": reverse_lazy("admin:awzm_bar_changelist"),
                },
            ],
        }],
}
