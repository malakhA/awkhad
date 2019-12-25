# -*- coding: utf-8 -*-

from awkhad import models, fields, api


class SetupBarBankConfigWizard(models.TransientModel):
    _inherit = 'account.setup.bank.manual.config'

    def validate(self):
        """ Default the bank statement source of new bank journals as 'file_import'
        """
        super(SetupBarBankConfigWizard, self).validate()
        if (self.create_or_link_option == 'new' or self.linked_journal_id.bank_statements_source == 'undefined') \
          and self.env['account.journal']._get_bank_statements_available_import_formats():
            self.linked_journal_id.bank_statements_source = 'file_import'
