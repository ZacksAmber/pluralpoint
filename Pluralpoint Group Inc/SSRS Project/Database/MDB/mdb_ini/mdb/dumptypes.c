/******************************************************************/
/* THIS IS AN AUTOMATICALLY GENERATED FILE.  DO NOT EDIT IT!!!!!! */
/******************************************************************/
#include <stdio.h>
#include "dumptypes.h"
void dump_Credit (Credit x)
{
	fprintf (stdout, "**************** Credit ****************\n");
	fprintf (stdout, "x.credit authorization number = ");
	dump_string (x.credit authorization number);
	fprintf (stdout, "x.customer credit id = ");
	dump_long (x.customer credit id);
	fprintf (stdout, "x.amount = ");
amount);
}

void dump_Customer (Customer x)
{
	fprintf (stdout, "**************** Customer ****************\n");
	fprintf (stdout, "x.customer id = ");
	dump_long (x.customer id);
	fprintf (stdout, "x.customer credit id = ");
	dump_long (x.customer credit id);
	fprintf (stdout, "x.customer name = ");
	dump_string (x.customer name);
	fprintf (stdout, "x.contact first name = ");
	dump_string (x.contact first name);
	fprintf (stdout, "x.contact last name = ");
	dump_string (x.contact last name);
	fprintf (stdout, "x.contact title = ");
	dump_string (x.contact title);
	fprintf (stdout, "x.contact position = ");
	dump_string (x.contact position);
	fprintf (stdout, "x.last year sales = ");
last year sales);
	fprintf (stdout, "x.address1 = ");
	dump_string (x.address1);
	fprintf (stdout, "x.address2 = ");
	dump_string (x.address2);
	fprintf (stdout, "x.city = ");
	dump_string (x.city);
	fprintf (stdout, "x.region = ");
	dump_string (x.region);
	fprintf (stdout, "x.country = ");
	dump_string (x.country);
	fprintf (stdout, "x.postal code = ");
	dump_string (x.postal code);
	fprintf (stdout, "x.email = ");
	dump_string (x.email);
	fprintf (stdout, "x.web site = ");
	dump_string (x.web site);
	fprintf (stdout, "x.phone = ");
	dump_string (x.phone);
	fprintf (stdout, "x.fax = ");
	dump_string (x.fax);
}

void dump_Employee Addresses (Employee Addresses x)
{
	fprintf (stdout, "**************** Employee Addresses ****************\n");
	fprintf (stdout, "x.employee id = ");
	dump_long (x.employee id);
	fprintf (stdout, "x.address1 = ");
	dump_string (x.address1);
	fprintf (stdout, "x.address2 = ");
	dump_string (x.address2);
	fprintf (stdout, "x.city = ");
	dump_string (x.city);
	fprintf (stdout, "x.region = ");
	dump_string (x.region);
	fprintf (stdout, "x.country = ");
	dump_string (x.country);
	fprintf (stdout, "x.postal code = ");
	dump_string (x.postal code);
	fprintf (stdout, "x.emergency contact address1 = ");
	dump_string (x.emergency contact address1);
	fprintf (stdout, "x.emergency contact address2 = ");
	dump_string (x.emergency contact address2);
	fprintf (stdout, "x.emergency contact city = ");
	dump_string (x.emergency contact city);
	fprintf (stdout, "x.emergency contact region = ");
	dump_string (x.emergency contact region);
	fprintf (stdout, "x.emergency contact country = ");
	dump_string (x.emergency contact country);
	fprintf (stdout, "x.emergency contact postal code = ");
	dump_string (x.emergency contact postal code);
}

void dump_Financials (Financials x)
{
	fprintf (stdout, "**************** Financials ****************\n");
	fprintf (stdout, "x.company id = ");
	dump_string (x.company id);
	fprintf (stdout, "x.statement date = ");
statement date);
	fprintf (stdout, "x.cash = ");
cash);
	fprintf (stdout, "x.account receivable = ");
account receivable);
	fprintf (stdout, "x.inventories = ");
inventories);
	fprintf (stdout, "x.other current assets = ");
other current assets);
	fprintf (stdout, "x.land = ");
land);
	fprintf (stdout, "x.buildings = ");
buildings);
	fprintf (stdout, "x.machinery etc = ");
machinery etc);
	fprintf (stdout, "x.accumulated depreciation = ");
accumulated depreciation);
	fprintf (stdout, "x.other assets = ");
other assets);
	fprintf (stdout, "x.accounts payable = ");
accounts payable);
	fprintf (stdout, "x.accrued liabilities = ");
accrued liabilities);
	fprintf (stdout, "x.accrued income taxes = ");
accrued income taxes);
	fprintf (stdout, "x.notes payable = ");
notes payable);
	fprintf (stdout, "x.deferred income taxes = ");
deferred income taxes);
	fprintf (stdout, "x.preferred stock = ");
preferred stock);
	fprintf (stdout, "x.common stock = ");
common stock);
	fprintf (stdout, "x.retained earnings = ");
retained earnings);
	fprintf (stdout, "x.net sales = ");
net sales);
	fprintf (stdout, "x.cogs = ");
cogs);
	fprintf (stdout, "x.general expenses = ");
general expenses);
	fprintf (stdout, "x.depreciation = ");
depreciation);
	fprintf (stdout, "x.interest expenses = ");
interest expenses);
	fprintf (stdout, "x.other income expenses = ");
other income expenses);
	fprintf (stdout, "x.taxes = ");
taxes);
}

void dump_Orders (Orders x)
{
	fprintf (stdout, "**************** Orders ****************\n");
	fprintf (stdout, "x.order id = ");
	dump_long (x.order id);
	fprintf (stdout, "x.order amount = ");
order amount);
	fprintf (stdout, "x.customer id = ");
	dump_long (x.customer id);
	fprintf (stdout, "x.employee id = ");
	dump_long (x.employee id);
	fprintf (stdout, "x.order date = ");
order date);
	fprintf (stdout, "x.required date = ");
required date);
	fprintf (stdout, "x.ship date = ");
ship date);
	fprintf (stdout, "x.courier website = ");
	dump_string (x.courier website);
	fprintf (stdout, "x.ship via = ");
	dump_string (x.ship via);
	fprintf (stdout, "x.shipped = ");
shipped);
	fprintf (stdout, "x.po = ");
	dump_string (x.po);
	fprintf (stdout, "x.payment received = ");
payment received);
}

void dump_Orders Detail (Orders Detail x)
{
	fprintf (stdout, "**************** Orders Detail ****************\n");
	fprintf (stdout, "x.order id = ");
	dump_long (x.order id);
	fprintf (stdout, "x.product id = ");
	dump_long (x.product id);
	fprintf (stdout, "x.unit price = ");
unit price);
	fprintf (stdout, "x.quantity = ");
	dump_long (x.quantity);
}

void dump_Product Type (Product Type x)
{
	fprintf (stdout, "**************** Product Type ****************\n");
	fprintf (stdout, "x.product type id = ");
	dump_long (x.product type id);
	fprintf (stdout, "x.product type name = ");
	dump_string (x.product type name);
	fprintf (stdout, "x.description = ");
	dump_string (x.description);
	fprintf (stdout, "x.picture = ");
picture);
}

void dump_Purchases (Purchases x)
{
	fprintf (stdout, "**************** Purchases ****************\n");
	fprintf (stdout, "x.product id = ");
	dump_long (x.product id);
	fprintf (stdout, "x.reorder level = ");
	dump_long (x.reorder level);
	fprintf (stdout, "x.units in stock = ");
	dump_long (x.units in stock);
	fprintf (stdout, "x.units on order = ");
	dump_long (x.units on order);
	fprintf (stdout, "x.po = ");
	dump_long (x.po);
	fprintf (stdout, "x.order date = ");
order date);
	fprintf (stdout, "x.expected receiving date = ");
expected receiving date);
	fprintf (stdout, "x.received = ");
received);
	fprintf (stdout, "x.paid = ");
paid);
}

void dump_Supplier (Supplier x)
{
	fprintf (stdout, "**************** Supplier ****************\n");
	fprintf (stdout, "x.supplier id = ");
	dump_long (x.supplier id);
	fprintf (stdout, "x.supplier name = ");
	dump_string (x.supplier name);
	fprintf (stdout, "x.address1 = ");
	dump_string (x.address1);
	fprintf (stdout, "x.address2 = ");
	dump_string (x.address2);
	fprintf (stdout, "x.city = ");
	dump_string (x.city);
	fprintf (stdout, "x.region = ");
	dump_string (x.region);
	fprintf (stdout, "x.country = ");
	dump_string (x.country);
	fprintf (stdout, "x.postal code = ");
	dump_string (x.postal code);
	fprintf (stdout, "x.phone = ");
	dump_string (x.phone);
}

void dump_Employee (Employee x)
{
	fprintf (stdout, "**************** Employee ****************\n");
	fprintf (stdout, "x.employee id = ");
	dump_long (x.employee id);
	fprintf (stdout, "x.supervisor id = ");
	dump_long (x.supervisor id);
	fprintf (stdout, "x.last name = ");
	dump_string (x.last name);
	fprintf (stdout, "x.first name = ");
	dump_string (x.first name);
	fprintf (stdout, "x.position = ");
	dump_string (x.position);
	fprintf (stdout, "x.birth date = ");
birth date);
	fprintf (stdout, "x.hire date = ");
hire date);
	fprintf (stdout, "x.home phone = ");
	dump_string (x.home phone);
	fprintf (stdout, "x.extension = ");
	dump_string (x.extension);
	fprintf (stdout, "x.photo = ");
photo);
	fprintf (stdout, "x.notes = ");
	dump_string (x.notes);
	fprintf (stdout, "x.reports to = ");
	dump_long (x.reports to);
	fprintf (stdout, "x.salary = ");
salary);
	fprintf (stdout, "x.ssn = ");
	dump_string (x.ssn);
	fprintf (stdout, "x.emergency contact first name = ");
	dump_string (x.emergency contact first name);
	fprintf (stdout, "x.emergency contact last name = ");
	dump_string (x.emergency contact last name);
	fprintf (stdout, "x.emergency contact relationship = ");
	dump_string (x.emergency contact relationship);
	fprintf (stdout, "x.emergency contact phone = ");
	dump_string (x.emergency contact phone);
}

void dump_Product (Product x)
{
	fprintf (stdout, "**************** Product ****************\n");
	fprintf (stdout, "x.product id = ");
	dump_long (x.product id);
	fprintf (stdout, "x.product name = ");
	dump_string (x.product name);
	fprintf (stdout, "x.color = ");
	dump_string (x.color);
	fprintf (stdout, "x.size = ");
	dump_string (x.size);
	fprintf (stdout, "x.mf = ");
	dump_string (x.mf);
	fprintf (stdout, "x.price = ");
price);
	fprintf (stdout, "x.product type id = ");
	dump_long (x.product type id);
	fprintf (stdout, "x.product class = ");
	dump_string (x.product class);
	fprintf (stdout, "x.supplier id = ");
	dump_long (x.supplier id);
}

void dump_Xtreme Info (Xtreme Info x)
{
	fprintf (stdout, "**************** Xtreme Info ****************\n");
	fprintf (stdout, "x.xtreme name = ");
	dump_string (x.xtreme name);
	fprintf (stdout, "x.address = ");
	dump_string (x.address);
	fprintf (stdout, "x.city = ");
	dump_string (x.city);
	fprintf (stdout, "x.province = ");
	dump_string (x.province);
	fprintf (stdout, "x.country = ");
	dump_string (x.country);
	fprintf (stdout, "x.postal code = ");
	dump_string (x.postal code);
	fprintf (stdout, "x.phone = ");
	dump_string (x.phone);
	fprintf (stdout, "x.fax = ");
	dump_string (x.fax);
	fprintf (stdout, "x.logo b&w = ");
logo b&w);
	fprintf (stdout, "x.logo color = ");
logo color);
}

