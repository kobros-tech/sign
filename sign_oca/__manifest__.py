# Copyright 2023 Dixmit
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Sign Oca",
    "summary": """
        Allow to sign documents inside Odoo CE""",
    "version": "18.0.1.0.0",
    "license": "AGPL-3",
    "author": "Dixmit,Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/sign",
    "depends": ["web_editor", "portal", "base_sparse_field", "bus"],
    "data": [
        "security/security.xml",
        "views/menu.xml",
        "data/data.xml",
        "wizards/res_config_settings_views.xml",
        "data/ir_sequence_data.xml",
        "wizards/sign_oca_template_generate.xml",
        "wizards/sign_oca_template_generate_multi.xml",
        "views/res_partner_views.xml",
        "views/sign_oca_request_log.xml",
        "views/sign_oca_request.xml",
        "security/ir.model.access.csv",
        "views/sign_oca_field.xml",
        "views/sign_oca_role.xml",
        "views/sign_oca_template.xml",
        "templates/assets.xml",
    ],
    "demo": [
        "demo/sign_oca_template.xml",
    ],
    "assets": {
        "web.assets_backend": [
            ("include", "web._assets_jquery"),
            "sign_oca/static/src/components/sign_oca_pdf_common/sign_oca_pdf_common.xml",
            "sign_oca/static/src/components/sign_oca_configure/sign_oca_configure.xml",
            "sign_oca/static/src/components/sign_oca_pdf/sign_oca_pdf.xml",
            "sign_oca/static/src/elements/elements.xml",
            "sign_oca/static/src/scss/sign_oca.scss",
            "sign_oca/static/src/components/sign_oca_pdf_common/sign_oca_pdf_common.esm.js",
            "sign_oca/static/src/components/sign_oca_configure/sign_oca_configure_field_dialog.esm.js",
            "sign_oca/static/src/components/sign_oca_configure/sign_oca_configure_field_dialog.xml",
            "sign_oca/static/src/components/sign_oca_configure/sign_oca_configure.esm.js",
            "sign_oca/static/src/components/sign_oca_preview/sign_oca_preview.esm.js",
            "sign_oca/static/src/components/sign_oca_preview/sign_oca_preview.xml",
            "sign_oca/static/src/elements/text.esm.js",
            "sign_oca/static/src/elements/signature.esm.js",
            "sign_oca/static/src/elements/check.esm.js",
            "sign_oca/static/src/components/sign_oca_pdf/sign_oca_pdf.esm.js",
            "sign_oca/static/src/js/sign_requests_service.esm.js",
            "sign_oca/static/src/js/sign_oca.esm.js",
            "sign_oca/static/src/js/systray_service.esm.js",
            "sign_oca/static/src/xml/*.xml",
        ],
        "oca_sign.assets_frontend_sign": [
            # frontend needed imports
            ("include", "web._assets_helpers"),
            ("include", "web._assets_primary_variables"),
            ("include", "web._assets_frontend_helpers"),
            "web/static/lib/jquery/jquery.js",
            "web/static/src/scss/pre_variables.scss",
            "web/static/lib/bootstrap/scss/_variables.scss",
            "web/static/lib/bootstrap/scss/_variables-dark.scss",
            "web/static/lib/bootstrap/scss/_maps.scss",
            ("include", "web._assets_bootstrap_frontend"),
            ("include", "web._assets_bootstrap_backend"),
            "web/static/lib/odoo_ui_icons/*",
            "web/static/lib/bootstrap/scss/_functions.scss",
            "web/static/lib/bootstrap/scss/_mixins.scss",
            "web/static/lib/bootstrap/scss/utilities/_api.scss",
            "web/static/src/libs/fontawesome/css/font-awesome.css",
            ("include", "web._assets_core"),
            # especific module frontend imports
            "sign_oca/static/src/components/sign_oca_pdf_common/sign_oca_pdf_common.xml",
            "sign_oca/static/src/components/sign_oca_configure/sign_oca_configure.xml",
            "sign_oca/static/src/components/sign_oca_pdf/sign_oca_pdf.xml",
            "sign_oca/static/src/components/sign_oca_pdf_portal/sign_oca_pdf_portal.xml",
            "sign_oca/static/src/elements/elements.xml",
            "sign_oca/static/src/scss/sign_oca.scss",
            "sign_oca/static/src/components/sign_oca_pdf_common/sign_oca_pdf_common.esm.js",
            "sign_oca/static/src/elements/text.esm.js",
            "sign_oca/static/src/elements/signature.esm.js",
            "sign_oca/static/src/elements/check.esm.js",
            "sign_oca/static/src/components/sign_oca_pdf/sign_oca_pdf.esm.js",
            "sign_oca/static/src/components/sign_oca_pdf_portal/sign_oca_pdf_portal.esm.js",
            "sign_oca/static/src/scss/portal.scss",
            "sign_oca/static/src/xml/*.xml",
        ],
        "sign_oca.sign_assets": [
            "sign_oca/static/src/scss/sign.scss",
            "web/static/src/libs/fontawesome/css/font-awesome.css",
        ],
    },
    "maintainers": ["etobella"],
}
