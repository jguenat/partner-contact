import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo8-addons-oca-partner-contact",
    description="Meta package for oca-partner-contact Odoo addons",
    version=version,
    install_requires=[
        'odoo8-addon-base_contact',
        'odoo8-addon-base_continent',
        'odoo8-addon-base_location',
        'odoo8-addon-base_location_geonames_import',
        'odoo8-addon-base_location_lau',
        'odoo8-addon-base_location_nuts',
        'odoo8-addon-base_partner_merge',
        'odoo8-addon-base_partner_sequence',
        'odoo8-addon-base_vat_sanitized',
        'odoo8-addon-partner_academic_title',
        'odoo8-addon-partner_address_street3',
        'odoo8-addon-partner_auto_salesman',
        'odoo8-addon-partner_capital',
        'odoo8-addon-partner_changeset',
        'odoo8-addon-partner_coc',
        'odoo8-addon-partner_contact_address_detailed',
        'odoo8-addon-partner_contact_birthdate',
        'odoo8-addon-partner_contact_department',
        'odoo8-addon-partner_contact_gender',
        'odoo8-addon-partner_contact_in_several_companies',
        'odoo8-addon-partner_contact_job_position',
        'odoo8-addon-partner_contact_lang',
        'odoo8-addon-partner_contact_nationality',
        'odoo8-addon-partner_contact_personal_information_page',
        'odoo8-addon-partner_create_by_vat',
        'odoo8-addon-partner_default_sale_discount',
        'odoo8-addon-partner_employee_quantity',
        'odoo8-addon-partner_external_maps',
        'odoo8-addon-partner_financial_risk',
        'odoo8-addon-partner_firstname',
        'odoo8-addon-partner_helper',
        'odoo8-addon-partner_identification',
        'odoo8-addon-partner_identification_gln',
        'odoo8-addon-partner_noncommercial',
        'odoo8-addon-partner_phone_extension',
        'odoo8-addon-partner_relations',
        'odoo8-addon-partner_sale_risk',
        'odoo8-addon-partner_second_lastname',
        'odoo8-addon-partner_sector',
        'odoo8-addon-partner_street_number',
        'odoo8-addon-partner_tag_actions',
        'odoo8-addon-passport',
        'odoo8-addon-portal_partner_merge',
        'odoo8-addon-res_partner_affiliate',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 8.0',
    ]
)
