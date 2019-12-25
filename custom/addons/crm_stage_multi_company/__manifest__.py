# Copyright 2019 ACS0NE SA/NV
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Crm Stage Multi Company",
    "summary": """
        This module adds support for multi company on crm stage.""",
    "version": "12.0.1.0.0",
    "license": "AGPL-3",
    "author": "ACS0NE SA/NV, Awkhad Community Association (ACA)",
    "website": "https://github.com/ACA/multi-company",
    "application": False,
    "installable": True,
    "depends": ["crm"],
    "data": ["views/crm_stage.xml", "security/crm_security.xml"],
    "demo": [],
}
