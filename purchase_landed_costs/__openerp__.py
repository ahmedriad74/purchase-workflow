# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2010-2013 Camptocamp (<http://www.camptocamp.com>)
#    Authors: Ferdinand Gasauer, Joel Grand-Guillaume
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
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


{
    'name': 'Purchase Landed Costs',
    'version': '1.0',
    'category': 'Warehouse Management',
    'description': """
Purchase Landed Costs
=====================

This module adds the possibility to include estimated landed costs in the average price computation. To
define those landed costs, create products for every landed costs and affect them a distribution type.
Don't forget to as well assign them a specific financial account (the one which will record the real cost) 
in order to compare at the end of the year the estimation with real accounting entries (see stock valuation).

The landed costs can be defined in purchase orders. Those costs will be distributed according to the
distribution type defined in landed cost:

 * value - example custom fees
 * quantity - example freight

For each landed cost position define in a PO, a draft invoice can be created in validation of purchase
order (an option need to be checked). Those invoice will then appear using the view invoice button of PO.

The products used to define landed cost must be classified "Distribution Type" as :

 * "Value" (for customs) or 
 * "Quantity" (for freight)

You can define landed cost relative to a whole PO or by line (or both) and the system will distribute
them to each line according to the chosen distribution type. 

Note that the landed cost is always expressed in company currency.

Find all landed cost here : Reporting -> Purchase -> Landed costs

Stock valuation:
----------------
As the Average price is also used for the stock valuation and because the computation is based on estimation
of landed cost in the PO (done at incomming shippment reception), you will have a little difference between
accounting and stock valuation that will need to be corrected when making the stock accounting entry. To 
correct that amount, make a sum of estimated landed cost (landed cost position) by account and compare with 
the real account chart value. You can acces those informations through this menu: Reporting -> Purchase -> Landed costs

Warning:
--------

 * Average price will be computed based on the estimation made on the PO, not from
  real cost. This is due to the way OpenERP compute average stock : it stores the updated
  value at every input, no history, so no way to redefine the value afterwards. e.g.
    - incomming 01: 100 product A at 50.- AVG = 50.-, stock = 100
    - incomming 02: 100 product A at 60.- AVG = 55.-, stock = 200
    - delivery 01: 50 product A AVG = 55.-, stock = 150
    - Receive the real landed cost of 10.- for incomming 01 
  => cannot compute back because no historical price was store for every transaction. Moreover, in OpenERP I can even 
  set another average price for a product using the update wizard.


 * As the price type of OpenERP is not really well handled, we need to be sure that price type of cost price in product form
   is the same as the company one. Otherwise, when computing the AVG price, it make the convertion in company currency
   from the price type currency. This is not related to this module, but from the core of OpenERP.

TODO/Ideas:
-----------
 * Manage multi-currencies in landed costs
 * Have the shipped date in landed cost instead of PO date for a better analysis
 * Compute a average purchase price per products while keep cost price as it is now
""",
    'author': 'Camptocamp',
    'depends': ['purchase' ],
    'website': 'http://www.camptocamp.com',
    'data': ['security/ir.model.access.csv',
             'security/landed_cost_security.xml',
             'purchase_view.xml',
            ],
    'test': [
        'test/landed_costs_based_on_quantity.yml',
        'test/landed_costs_based_on_value.yml',
        'test/landed_costs_on qty_by_line_and_order.yml',
    ],
    'demo': [],
    'installable': True,
    'active': False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
