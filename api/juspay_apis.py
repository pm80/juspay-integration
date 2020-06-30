import os

import requests

API_KEY_SANDBOX = os.getenv("API_KEY_SANDBOX")
API_KEY_PRODUCTION = os.getenv("")

MERCHANT_ID_SANDBOX = os.getenv("MERCHANT_ID_SANDBOX")
MERCHANT_ID_PRODUCTION = os.getenv("MERCHANT_ID_PRODUCTION")

ENV = 'sandbox'


def get_api_key(env=ENV):
    if env == 'sandbox':
        return API_KEY_SANDBOX
    elif env == 'production':
        return API_KEY_PRODUCTION
    raise ValueError('env can only be one of these: ["sandbox", "production"]')


def get_merchant_id(env=ENV):
    if env == 'sandbox':
        return MERCHANT_ID_SANDBOX
    elif env == 'production':
        return MERCHANT_ID_PRODUCTION
    raise ValueError('env can only be one of these: ["sandbox", "production"]')


def get_base_url(env=ENV):
    if env == 'sandbox':
        return 'https://sandbox.juspay.in'
    elif env == 'production':
        return 'https://api.juspay.in'
    raise ValueError('env can only be one of these: ["sandbox", "production"]')


class Orders:
    @classmethod
    def create_order(cls,
                     order_id,
                     order_amount,
                     currency='INR',
                     customer_id=None,
                     customer_email=None,
                     customer_phone=None,
                     description=None,
                     product_id=None,
                     gateway_id=None,
                     return_url=None,
                     billing_address_first_name=None,
                     billing_address_last_name=None,
                     billing_address_line1=None,
                     billing_address_line2=None,
                     billing_address_line3=None,
                     billing_address_city=None,
                     billing_address_state=None,
                     billing_address_country=None,
                     billing_address_postal_code=None,
                     billing_address_phone=None,
                     billing_address_country_code_iso=None,
                     shipping_address_first_name=None,
                     shipping_address_last_name=None,
                     shipping_address_line1=None,
                     shipping_address_line2=None,
                     shipping_address_line3=None,
                     shipping_address_city=None,
                     shipping_address_state=None,
                     shipping_address_country=None,
                     shipping_address_postal_code=None,
                     shipping_address_phone=None,
                     shipping_address_country_code_iso=None,
                     option_get_client_auth_token=False,
                     udf1=None,
                     udf2=None,
                     udf3=None,
                     udf4=None,
                     udf5=None,
                     udf6=None,
                     udf7=None,
                     udf8=None,
                     udf9=None,
                     udf10=None,
                     env=ENV,
                     res_format='json'):
        params = (
            ('options.get_client_auth_token', option_get_client_auth_token),
        )

        data = {
            'order_id': order_id,
            'amount': order_amount,
            'currency': currency,
            'customer_id': customer_id,
            'customer_email': customer_email,
            'customer_phone': customer_phone,
            'description': description,
            'product_id': product_id,
            'gateway_id': gateway_id,
            'return_url': return_url,
            'billing_address_first_name': billing_address_first_name,
            'billing_address_last_name': billing_address_last_name,
            'billing_address_line1': billing_address_line1,
            'billing_address_line2': billing_address_line2,
            'billing_address_line3': billing_address_line3,
            'billing_address_city': billing_address_city,
            'billing_address_state': billing_address_state,
            'billing_address_country': billing_address_country,
            'billing_address_postal_code': billing_address_postal_code,
            'billing_address_phone': billing_address_phone,
            'billing_address_country_code_iso': billing_address_country_code_iso,
            'shipping_address_first_name': shipping_address_first_name,
            'shipping_address_last_name': shipping_address_last_name,
            'shipping_address_line1': shipping_address_line1,
            'shipping_address_line2': shipping_address_line2,
            'shipping_address_line3': shipping_address_line3,
            'shipping_address_city': shipping_address_city,
            'shipping_address_state': shipping_address_state,
            'shipping_address_country': shipping_address_country,
            'shipping_address_postal_code': shipping_address_postal_code,
            'shipping_address_phone': shipping_address_phone,
            'shipping_address_country_code_iso': shipping_address_country_code_iso,
            'udf1': udf1,
            'udf2': udf2,
            'udf3': udf3,
            'udf4': udf4,
            'udf5': udf5,
            'udf6': udf6,
            'udf7': udf7,
            'udf8': udf8,
            'udf9': udf9,
            'udf10': udf10,
        }

        url = get_base_url(env=env) + '/orders'
        response = requests.post(url, params=params, data=data, auth=(get_api_key(env=env), ''))
        return response.json() if res_format == 'json' else response

    @classmethod
    def get_order_status(cls, order_id, env=ENV, res_format='json'):
        url = get_base_url(env=env) + f'/orders/{order_id}'
        response = requests.get(url, auth=(get_api_key(env=env), ''))
        return response.json() if res_format == 'json' else response

    @classmethod
    def update_order(cls,
                     order_id,
                     amount,
                     billing_address_first_name=None,
                     billing_address_last_name=None,
                     billing_address_line1=None,
                     billing_address_line2=None,
                     billing_address_line3=None,
                     billing_address_city=None,
                     billing_address_state=None,
                     billing_address_country=None,
                     billing_address_postal_code=None,
                     billing_address_phone=None,
                     billing_address_country_code_iso=None,
                     shipping_address_first_name=None,
                     shipping_address_last_name=None,
                     shipping_address_line1=None,
                     shipping_address_line2=None,
                     shipping_address_line3=None,
                     shipping_address_city=None,
                     shipping_address_state=None,
                     shipping_address_country=None,
                     shipping_address_postal_code=None,
                     shipping_address_phone=None,
                     shipping_address_country_code_iso=None,
                     udf1=None,
                     udf2=None,
                     udf3=None,
                     udf4=None,
                     udf5=None,
                     udf6=None,
                     udf7=None,
                     udf8=None,
                     udf9=None,
                     udf10=None,
                     env=ENV,
                     res_format='json'):
        data = {
            'order_id': order_id,
            'amount': amount,
            'billing_address_first_name': billing_address_first_name,
            'billing_address_last_name': billing_address_last_name,
            'billing_address_line1': billing_address_line1,
            'billing_address_line2': billing_address_line2,
            'billing_address_line3': billing_address_line3,
            'billing_address_city': billing_address_city,
            'billing_address_state': billing_address_state,
            'billing_address_country': billing_address_country,
            'billing_address_postal_code': billing_address_postal_code,
            'billing_address_phone': billing_address_phone,
            'billing_address_country_code_iso': billing_address_country_code_iso,
            'shipping_address_first_name': shipping_address_first_name,
            'shipping_address_last_name': shipping_address_last_name,
            'shipping_address_line1': shipping_address_line1,
            'shipping_address_line2': shipping_address_line2,
            'shipping_address_line3': shipping_address_line3,
            'shipping_address_city': shipping_address_city,
            'shipping_address_state': shipping_address_state,
            'shipping_address_country': shipping_address_country,
            'shipping_address_postal_code': shipping_address_postal_code,
            'shipping_address_phone': shipping_address_phone,
            'shipping_address_country_code_iso': shipping_address_country_code_iso,
            'udf1': udf1,
            'udf2': udf2,
            'udf3': udf3,
            'udf4': udf4,
            'udf5': udf5,
            'udf6': udf6,
            'udf7': udf7,
            'udf8': udf8,
            'udf9': udf9,
            'udf10': udf10
        }

        url = get_base_url(env=env) + f'/orders/{order_id}'
        response = requests.post(url, data=data, auth=(get_api_key(env=env), ''))
        return response.json() if res_format == 'json' else response

    @classmethod
    def refund_order(cls,
                     order_id,
                     unique_request_id,
                     amount=None,
                     env=ENV,
                     res_format='json'):
        headers = {
            'version': '2018-10-25',
        }

        data = {
            'unique_request_id': unique_request_id,
            'amount': amount
        }

        url = get_base_url(env=env) + f'/orders/{order_id}/refunds'
        print("url  ", url)
        response = requests.post(url, headers=headers, data=data, auth=(get_api_key(env=env), ''))
        return response.json() if res_format == 'json' else response


class Customer:
    @classmethod
    def create_customer(cls,
                        object_reference_id,
                        merchant_id,
                        mobile_number,
                        email_address=None,
                        first_name=None,
                        last_name=None,
                        mobile_country_code=None,
                        option_get_client_auth_token=False,
                        env=ENV,
                        res_format='json'):
        params = (
            ('options.get_client_auth_token', option_get_client_auth_token),
        )

        headers = {
            'x-merchantid': merchant_id,
        }

        data = {
            'object_reference_id': object_reference_id,
            'mobile_number': mobile_number,
            'email_address': email_address,
            'first_name': first_name,
            'last_name': last_name,
            'mobile_country_code': mobile_country_code,
        }

        url = get_base_url(env=env) + '/customers'
        response = requests.post(url, params=params, headers=headers, data=data, auth=(get_api_key(env=env), ''))
        return response.json() if res_format == 'json' else response

    @classmethod
    def get_customer(cls,
                     customer_id,
                     merchant_id,
                     option_get_client_auth_token=False,
                     env=ENV,
                     res_format='json'):
        params = (
            ('options.get_client_auth_token', option_get_client_auth_token),
        )

        headers = {
            'x-merchantid': merchant_id,
        }

        url = get_base_url(env=env) + f'/customers/{customer_id}'
        response = requests.get(url, params=params, headers=headers, auth=(get_api_key(env=env), ''))
        return response.json() if res_format == 'json' else response

    @classmethod
    def update_customer(cls,
                        customer_id,
                        mobile_number=None,
                        email_address=None,
                        first_name=None,
                        last_name=None,
                        mobile_country_code=None,
                        env=ENV,
                        res_format='json'):
        data = {
            'mobile_number': mobile_number,
            'email_address': email_address,
            'first_name': first_name,
            'last_name': last_name,
            'mobile_country_code': mobile_country_code
        }

        url = get_base_url(env=env) + f'/customers/{customer_id}'
        response = requests.post(url, data=data, auth=(get_api_key(env=env), ''))
        return response.json() if res_format == 'json' else response


class Card:
    class AuthType(enumerate):
        OTP = 'OTP'
        VIES = 'VIES'

    @classmethod
    def tokenize(cls,
                 merchant_id,
                 card_number,
                 card_exp_year,
                 card_exp_month,
                 card_security_code,
                 name_on_card,
                 env=ENV,
                 res_format='json'):
        data = {
            'merchant_id': merchant_id,
            'card_number': card_number,
            'card_exp_year': card_exp_year,
            'card_exp_month': card_exp_month,
            'card_security_code': card_security_code,
            'name_on_card': name_on_card,
        }

        url = get_base_url(env=env) + '/card/tokenize'
        response = requests.post(url, data=data)
        return response.json() if res_format == 'json' else response

    @classmethod
    def add_card(cls,
                 merchant_id,
                 customer_id,
                 card_number,
                 card_exp_year,
                 card_exp_month,
                 customer_email=None,
                 name_on_card=None,
                 nickname=None,
                 env=ENV,
                 res_format='json'):
        data = {
            'merchant_id': merchant_id,
            'customer_id': customer_id,
            'customer_email': customer_email,
            'card_number': card_number,
            'card_exp_year': card_exp_year,
            'card_exp_month': card_exp_month,
            'name_on_card': name_on_card,
            'nickname': nickname,
        }

        url = get_base_url(env=env) + '/card/add'
        response = requests.post(url, data=data, auth=(get_api_key(env=env), ''))
        return response.json() if res_format == 'json' else response

    @classmethod
    def list_stored_cards(cls,
                          customer_id,
                          option_check_mandate_support=True,
                          env=ENV,
                          res_format='json'):
        params = (
            ('customer_id', customer_id),
            ('options.check_mandate_support', option_check_mandate_support),
        )

        url = get_base_url(env=env) + '/cards'
        response = requests.get(url, params=params, auth=(get_api_key(env=env), ''))
        return response.json() if res_format == 'json' else response

    @classmethod
    def delete_card(cls,
                    card_token,
                    env=ENV,
                    res_format='json'):
        data = {
            'card_token': card_token
        }

        url = get_base_url(env=env) + '/card/delete'
        response = requests.post(url, data=data, auth=(get_api_key(env=env), ''))
        return response.json() if res_format == 'json' else response

    @classmethod
    def card_info(cls,
                  cardbins,
                  merchant_id,
                  option_check_direct_otp_support=True,
                  option_check_mandate_support=True,
                  env=ENV,
                  res_format='json'):
        params = (
            ('merchant_id', merchant_id),
            ('options.check_direct_otp_support', option_check_direct_otp_support),
            ('options.check_mandate_support', option_check_mandate_support),
        )

        url = get_base_url(env=env) + f'/cardbins/{cardbins}'
        response = requests.get(url, params=params, auth=(get_api_key(env=env), ''))
        return response.json() if res_format == 'json' else response

    @classmethod
    def bin_list(cls,
                 auth_type: AuthType,
                 env=ENV,
                 res_format='json'):
        params = (
            ('auth_type', auth_type),
        )

        url = get_base_url(env=env) + f'/v2/bins/eligibility'
        response = requests.get(url, params=params, auth=(get_api_key(env=env), ''))
        return response.json() if res_format == 'json' else response


class Payments:
    class AuthType(enumerate):
        THREE_DS = 'THREE_DS'
        OTP = 'OTP'
        VISA_CHECKOUT = 'VISA_CHECKOUT'

    class EMIType(enumerate):
        STANDARD_EMI = 'STANDARD_EMI'
        NO_COST_EMI = 'NO_COST_EMI'

    @classmethod
    def card(cls,
             order_id,
             merchant_id,
             card_token=None,
             payment_method_type='CARD',
             payment_method=None,
             card_number=None,
             name_on_card=None,
             card_exp_year=None,
             card_exp_month=None,
             card_security_code=None,
             save_to_locker=None,
             redirect_after_payment=True,
             format='json',
             is_emi=None,
             emi_bank=None,
             emi_tenure=None,
             auth_type: AuthType = None,
             emi_type: EMIType = None,
             subvention_amount=None,
             env=ENV,
             res_format='json'):
        data = {
            'order_id': order_id,
            'merchant_id': merchant_id,
            'payment_method_type': payment_method_type,
            'payment_method': payment_method,
            'card_token': card_token,
            'card_number': card_number,
            'name_on_card': name_on_card,
            'card_exp_year': card_exp_year,
            'card_exp_month': card_exp_month,
            'card_security_code': card_security_code,
            'save_to_locker': save_to_locker,
            'redirect_after_payment': redirect_after_payment,
            'format': format,
            'is_emi': is_emi,
            'emi_bank': emi_bank,
            'emi_tenure': emi_tenure,
            'auth_type': auth_type,
            'emi_type': emi_type,
            'subvention_amount': subvention_amount,
        }

        url = get_base_url(env=env) + '/txns'
        response = requests.post(url, data=data, auth=(get_api_key(env=env), ''))
        return response.json() if res_format == 'json' else response

    @classmethod
    def netbanking(cls,
                   order_id,
                   merchant_id,
                   payment_method,
                   payment_method_type='NB',
                   redirect_after_payment=True,
                   format='json',
                   env=ENV,
                   res_format='json'):
        data = {
            'order_id': order_id,
            'merchant_id': merchant_id,
            'payment_method_type': payment_method_type,
            'payment_method': payment_method,
            'redirect_after_payment': redirect_after_payment,
            'format': format,
        }

        url = get_base_url(env=env) + '/txns'
        response = requests.post(url, data=data, auth=(get_api_key(env=env), ''))
        return response.json() if res_format == 'json' else response

    @classmethod
    def wallet_payment(cls,
                       order_id,
                       merchant_id,
                       authorization_key,
                       payment_method_type='WALLET',
                       payment_method=None,
                       redirect_after_payment=True,
                       format='json',
                       env=ENV,
                       res_format='json'):
        headers = {
            'content-type': "application/x-www-form-urlencoded",
            'authorization': f"Basic {authorization_key}"
        }

        data = {
            'order_id': order_id,
            'merchant_id': merchant_id,
            'payment_method_type': payment_method_type,
            'payment_method': payment_method,
            'redirect_after_payment': redirect_after_payment,
            'format': format,
        }

        url = get_base_url(env=env) + '/txns#WalletPayment'
        print(f'url for wallet payment : {url}')
        response = requests.post(url, headers=headers, data=data, auth=(get_api_key(env=env), ''))
        return response.json() if res_format == 'json' else response

    @classmethod
    def payment_methods(cls,
                        merchant_id='wakefit',
                        option_add_emandate_payment_methods=True,
                        option_check_wallet_direct_debit_support=True,
                        option_add_supported_reference_ids=True,
                        env=ENV,
                        res_format='json'):
        params = (
            ('options.add_emandate_payment_methods', option_add_emandate_payment_methods),
            ('options.check_wallet_direct_debit_support', option_check_wallet_direct_debit_support),
            ('options.add_supported_reference_ids', option_add_supported_reference_ids),
        )

        url = get_base_url(env=env) + f'/merchants/{merchant_id}/paymentmethods'
        response = requests.get(url, params=params, auth=(get_api_key(env=env), ''))
        return response.json() if res_format == 'json' else response


class Outages:
    @classmethod
    def list_outages(cls, env=ENV, res_format='json'):
        url = get_base_url(env=env) + '/outages'
        response = requests.get(url, auth=(get_api_key(env=env), ''))
        return response.json() if res_format == 'json' else response
