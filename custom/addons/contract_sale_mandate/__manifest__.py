# Copyright 2019 ACSONE SA/NV
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Contract Sale Mandate',
    'summary': """
        This module manages the banking mandate from the sale order to the
        contract.""",
    'version': '12.0.2.0.0',
    'license': 'AGPL-3',
    'author': 'ACSONE SA/NV,Awkhad Community Association (ACA)',
    'website': 'https://github.com/ACA/contract',
    'depends': [
        # ACA/bank-payment
        'account_banking_mandate',
        'account_banking_mandate_sale',
        # ACA/contract
        'contract',
        'contract_mandate',
        'product_contract',
    ],
}
