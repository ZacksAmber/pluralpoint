/******************************************************************/
/* THIS IS AN AUTOMATICALLY GENERATED FILE.  DO NOT EDIT IT!!!!!! */
/******************************************************************/
typedef struct _Credit
{
	char *	credit authorization number;
	long	customer credit id;
amount;

} Credit ;

typedef struct _Customer
{
	long	customer id;
	long	customer credit id;
	char *	customer name;
	char *	contact first name;
	char *	contact last name;
	char *	contact title;
	char *	contact position;
last year sales;
	char *	address1;
	char *	address2;
	char *	city;
	char *	region;
	char *	country;
	char *	postal code;
	char *	email;
	char *	web site;
	char *	phone;
	char *	fax;

} Customer ;

typedef struct _Employee Addresses
{
	long	employee id;
	char *	address1;
	char *	address2;
	char *	city;
	char *	region;
	char *	country;
	char *	postal code;
	char *	emergency contact address1;
	char *	emergency contact address2;
	char *	emergency contact city;
	char *	emergency contact region;
	char *	emergency contact country;
	char *	emergency contact postal code;

} Employee Addresses ;

typedef struct _Financials
{
	char *	company id;
statement date;
cash;
account receivable;
inventories;
other current assets;
land;
buildings;
machinery etc;
accumulated depreciation;
other assets;
accounts payable;
accrued liabilities;
accrued income taxes;
notes payable;
deferred income taxes;
preferred stock;
common stock;
retained earnings;
net sales;
cogs;
general expenses;
depreciation;
interest expenses;
other income expenses;
taxes;

} Financials ;

typedef struct _Orders
{
	long	order id;
order amount;
	long	customer id;
	long	employee id;
order date;
required date;
ship date;
	char *	courier website;
	char *	ship via;
shipped;
	char *	po;
payment received;

} Orders ;

typedef struct _Orders Detail
{
	long	order id;
	long	product id;
unit price;
	long	quantity;

} Orders Detail ;

typedef struct _Product Type
{
	long	product type id;
	char *	product type name;
	char *	description;
picture;

} Product Type ;

typedef struct _Purchases
{
	long	product id;
	long	reorder level;
	long	units in stock;
	long	units on order;
	long	po;
order date;
expected receiving date;
received;
paid;

} Purchases ;

typedef struct _Supplier
{
	long	supplier id;
	char *	supplier name;
	char *	address1;
	char *	address2;
	char *	city;
	char *	region;
	char *	country;
	char *	postal code;
	char *	phone;

} Supplier ;

typedef struct _Employee
{
	long	employee id;
	long	supervisor id;
	char *	last name;
	char *	first name;
	char *	position;
birth date;
hire date;
	char *	home phone;
	char *	extension;
photo;
	char *	notes;
	long	reports to;
salary;
	char *	ssn;
	char *	emergency contact first name;
	char *	emergency contact last name;
	char *	emergency contact relationship;
	char *	emergency contact phone;

} Employee ;

typedef struct _Product
{
	long	product id;
	char *	product name;
	char *	color;
	char *	size;
	char *	mf;
price;
	long	product type id;
	char *	product class;
	long	supplier id;

} Product ;

typedef struct _Xtreme Info
{
	char *	xtreme name;
	char *	address;
	char *	city;
	char *	province;
	char *	country;
	char *	postal code;
	char *	phone;
	char *	fax;
logo b&w;
logo color;

} Xtreme Info ;

