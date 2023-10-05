{
	'name' : 'Myanmar Application',
	'description' : 'My Company',
	'author' : 'Zin Moe Kyaw',
	'depends' : [
		'base_setup',
		'mail',
	],

	'data' : {
		'myanmar_view.xml',
		'singapore_view.xml',
		'education_foundation_view.xml',
		'employee_admin_view.xml',
		'security/ir.model.access.csv',
		'report/myanmar_report.xml',
	},
	'application' : True,
}