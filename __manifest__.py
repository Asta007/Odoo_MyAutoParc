# -*- coding: utf-8 -*-
{
    'name' : 'myautoparc',
    'version' : '1.3',
    'summary' : "parc management, tracking, ant rental",
    'sequence' : 1,
    'description' : "this module allows you to manage an automobil park, by providing you all the tools an parc need to get going without manually handling it yourself",
    'category' : 'ISI_ERP',
    'depends' : ['base'],
    'data' : [
        "security/ir.model.access.csv",
        "views/report/report_dashboard_template.xml",
        "views/report/report.xml",
        "views/client_views.xml",
        "views/model_views.xml",
        "views/brand_views.xml",
        "views/car_views.xml",
        "views/center_views.xml",
        "views/affectation_views.xml",
        "views/fuel_views.xml",
        "views/maintenance_views.xml",
        "views/document_views.xml",
        "views/employee_views.xml",
        "views/menu.xml"
    ],
    'installable' : True,
    'application' : True,
    'license' : 'LGPL-3',
    'Author' : 'TickingClock'
}