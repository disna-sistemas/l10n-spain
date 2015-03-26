# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (c) 2014 Domatix (http://www.domatix.com)
#                       Ángel Moya <angel.moya@domatix.com>
#    Copyright (c) 2015 Serv. Tecnol. Avanzados (http://www.serviciosbaeza.com)
#                       Pedro M. Baeza <pedro.baeza@serviciosbaeza.com>
#                       FactorLibre (http://factorlibre.com)
#                       Hugo Santos <hugo.santos@factorlibre.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp.osv import orm


class account_taxt(orm.Model):
    _inherit = 'account.tax'

    def name_get(self, cr, uid, ids, context=None):
        res = []
        for tax in self.browse(cr, uid, ids, context=context):
            res.append((tax.id, tax.name or tax.description))
        return res
