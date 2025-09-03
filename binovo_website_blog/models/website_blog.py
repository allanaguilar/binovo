# -*- coding: utf-8 -*-

from odoo import api, models, fields, _

class Blog(models.Model):
    _inherit = 'blog.blog'

    company_id = fields.Many2one('res.company', string='Company', default=lambda self: self.env.company, help="Company related to this blog.")

    @api.onchange('website_id')
    def _onchange_website_id(self):
        self.company_id = self.website_id.company_id
    
class BlogPost(models.Model):
    _inherit = "blog.post"

    company_id = fields.Many2one('res.company', string='Company', related="blog_id.company_id", store=True, readonly=False, help="Company related to this post.")