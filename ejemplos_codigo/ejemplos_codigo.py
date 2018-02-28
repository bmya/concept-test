"""
[20:23, 24/2/2018] Juan Scarafia: IMPLEMENTACIÓN ACTUAL:
En account document:

"""
    @api.multi
    def get_localization_invoice_vals(self):
        """
        Function to be inherited by different localizations and add custom
        data to invoice on invoice validation
        """
        self.ensure_one()
        return {}


"""
Luego en l10n_ar...
"""
    @api.multi
    def get_localization_invoice_vals(self):
        self.ensure_one()
        # TODO depreciar esta funcion y convertir a currency_rate campo
        # calculado que la calcule en funcion a los datos del move
        if self.localization == 'argentina':
            if self.company_id.currency_id == self.currency_id:
                currency_rate = 1.0


"""
O también algo tipo:
"""

    @api.multi
    def action_move_create(self):
        self.filtered(
            for rec in self.filtered(
                r.localization == 'argentina' and r.use_documents):
                # bla bla


"""
[20:23, 24/2/2018] Juan Scarafia: ALTERNATIVA 1
# metodo dummy en account_document
"""

    def action_confirm(self):
        localization = self.company_id.localization
        if hasattr(rec, '%s_action_confirm' % localization):
            getattr(self, '%s_action_confirm' % localization)()
        return super(AccountInvoice, self).action_confirm()


    # ej loc ar
    def argentina_action_confirm(self):
        # codigo especifico ar


"""
Alternativa 2
"""
    # metodo dummy en account_document
    def action_confirm(self):
        localization = self.company_id.localization

        if hasattr(rec, 'pre_%s_action_confirm' % localization):
            getattr(self, 'pre_%s_action_confirm' % localization)()
        res = super(AccountInvoice, self).action_confirm()

        if hasattr(rec, 'post_%s_action_confirm' % localization):
            getattr(self, 'post_%s_action_confirm' % localization)()
        return res


    # ej loc ar
    def pre_argentina_action_confirm(self):
        # codigo especifico ar pre confirmación factura

    # ej loc ar
    def post_argentina_action_confirm(self):
        # codigo especifico ar post confirmación factura
