{
	'name': 'zinmoe application',
	'description': 'zinmoe application sample',
	'author': 'Zin Moe Kyaw',
	'depends': [
		'base_setup',
		'mail',
	],

	'data': [
		'zinmoe_view.xml',
		'kyaw_view.xml',
		'background_education.xml',
		'employment_history_view.xml',
		'security/ir.model.access.csv',
		'report/zinmoe_report.xml',
		'report/kyaw_report.xml',
	],
	'application': True,
}