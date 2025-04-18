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
        "views/client_view.xml",
        "views/model_view.xml",
        "views/brand_view.xml",
        "views/car_view.xml"
    ],
    'installable' : True,
    'application' : True,
    'license' : 'LGPL-3',
    'Author' : 'TickingClock'
}