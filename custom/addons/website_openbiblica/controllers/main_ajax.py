# @http.route(['/somo_url'], type='json', auth="user", website=True)
# def input_data_processing(self, **kw):
#     cr, context, pool, uid = request.cr, request.context, request.registry, request.uid
#     # Fetch input json data sent from js
#     input_data = kw.get('input_data')
#     # Your code is here
#     return {
#         'output_data': output_data
#     }
from awkhad import http
from awkhad.http import request


class WebsiteBiblicaAjax(http.Controller):

    @http.route(['/get/langs'], type='json', auth="public", website=True)
    def language_data(self):
        # bibs = request.env['open.biblica'].sudo().search([])
        # lngs = request.env['res.lang'].sudo().search([('id', 'in', bibs.mapped('lang_id.id'))])
        lngs = request.env['res.lang'].sudo().search([])
        return lngs
            # {'lngs': lngs}
            # 'id': lngs.id,
            # 'name': lngs.name

