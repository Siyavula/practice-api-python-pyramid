import os
import requests

from pyramid.view import view_config


@view_config(route_name='get_question', renderer='/templates/practice_emas.jinja2')
@view_config(route_name='get_question_responsive', renderer='/templates/practice_emas.jinja2')
def get_question_responsive(request):
    template_id = 2122
    region = 'ZA'  # The country shortcode, can be either 'ZA', 'NG' or 'INTL'.
    curriculum = 'CAPS'  # The curriculum code, can be either 'CAPS', 'NG' or 'INTL'.
    # Use 'responsive' to get a responsive theme for modern devices
    # or 'basic' for older devices without JS support.
    theme = 'responsive'  # The theme to use, can be either 'responsive' or 'basic'.
    random_seed = 487029  # Random seed is optional, one will be generated if not provided.
    # Authentication payload
    data = {
        'name': os.environ['api_client_name'],
        'password': os.environ['api_client_password'],
        'client_ip': request.client_addr,
        'region': region,
        'curriculum': curriculum,
        'theme': theme
    }

    # Request token
    # res = requests.post('https://www.siyavula.com//api/practice/v1/get-token', json=data)
    res = requests.post(request.registry.settings[
                        'api_base_url'] + '/api/practice/v1/get-token', json=data, verify=False)
    token = res.json()['token']

    return {
        'token': token,
        'template_id': template_id,
        'random_seed': random_seed
    }


@view_config(route_name='get_question_basic', renderer='/templates/practice_mobile.jinja2')
def get_question_basic(request):
    template_id = 1805
    region = 'ZA'  # The country shortcode, can be either 'ZA', 'NG' or 'INTL'.
    curriculum = 'CAPS'  # The curriculum code, can be either 'CAPS', 'NG' or 'INTL'.
    # Use 'responsive' to get a responsive theme for modern devices
    # or 'basic' for older devices without JS support.
    theme = 'basic'  # The theme to use, can be either 'responsive' or 'basic'..
    random_seed = 259974  # Random seed is optional, one will be generated if not provided.
    # Authentication payload
    data = {
        'name': os.environ['api_client_name'],
        'password': os.environ['api_client_password'],
        'client_ip': request.client_addr,
        'region': region,
        'curriculum': curriculum,
        'theme': theme
    }

    # Request token
    res = requests.post(request.registry.settings['api_base_url'] + '/api/practice/v1/get-token',
                        json=data, verify=False)
    token = res.json()['token']

    # Set HTTP authentication(JWT) header
    headers = {'JWT': token}

    if request.POST:
        user_responses = {field: request.POST[field] for field in request.POST}

        # Submit answer payload
        data = {
            'template_id': template_id,
            'random_seed': random_seed,
            'user_responses': user_responses
        }
        # Submit answer
        res = requests.post(request.registry.settings['api_base_url'] + '/api/practice/v1/submit-answer',
                            json=data, headers=headers, verify=False)
        question_data = res.json()
    else:
        # Get question payload
        data = {
            'template_id': template_id,
            'random_seed': random_seed
        }
        # Get question data
        res = requests.post(request.registry.settings['api_base_url'] + '/api/practice/v1/get-question',
                            json=data, headers=headers, verify=False)
        question_data = res.json()

    return {
        'token': token,
        'template_id': template_id,
        'random_seed': random_seed,
        'question_html': question_data['question_html']
    }
