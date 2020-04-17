import requests

from pyramid.view import view_config

from practice_api_python_pyramid.config.credentials import api_client_name, api_client_password


@view_config(route_name='get_question', renderer='/templates/practice_emas.jinja2')
@view_config(route_name='get_question_emas', renderer='/templates/practice_emas.jinja2')
def get_question_emas(request):
    template_id = 2122
    region = 'ZA'  # The country shortcode, can be either 'ZA', 'NG' or 'INTL'.
    curriculum = 'CAPS'  # The curriculum code, can be either 'CAPS', 'NCS', 'IEB', 'NG' or 'INTL'.
    # Use emas for modern devices with JS support that supports responsive design
    # or mobi for older phones without JS support.
    theme = 'emas'  # The theme to use, can be either 'emas' or 'mobile'.
    random_seed = 487029  # Random seed is optional, one will be generated if not provided.
    # Authentication payload
    data = {
        'name': api_client_name,
        'password': api_client_password,
        'client_ip': request.client_addr,
        'region': region,
        'curriculum': curriculum,
        'theme': theme
    }

    # Request token
    # res = requests.post('https://www.siyavula.com//api/practice/v1/get-token', json=data)
    res = requests.post('https://www.emas/api/practice/v1/get-token', json=data, verify=False)
    token = res.json()['token']

    return {
        'token': token,
        'template_id': template_id,
        'random_seed': random_seed
    }


@view_config(route_name='get_question_mobile', renderer='/templates/practice_mobile.jinja2')
def get_question_mobile(request):
    template_id = 1805
    region = 'ZA'  # The country shortcode, can be either 'ZA', 'NG' or 'INTL'.
    curriculum = 'CAPS'  # The curriculum code, can be either 'CAPS', 'NCS', 'IEB', 'NG' or 'INTL'.
    # Use emas for modern devices with JS support that supports responsive design
    # or mobi for older phones without JS support.
    theme = 'emas'  # The theme to use, can be either 'emas' or 'mobile'.
    random_seed = 259974  # Random seed is optional, one will be generated if not provided.
    # Authentication payload
    data = {
        'name': api_client_name,
        'password': api_client_password,
        'client_ip': request.client_addr,
        'region': region,
        'curriculum': curriculum,
        'theme': 'mobile'
    }

    # Request token
    # res = requests.post('https://www.siyavula.com/api/practice/v1/get-token', json=data)
    res = requests.post('https://www.emas/api/practice/v1/get-token', json=data, verify=False)
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
        # res = requests.post('https://www.siyavula.com/api/practice/v1/submit-answer', json=data, headers=headers, verify=False)
        res = requests.post('https://www.emas/api/practice/v1/submit-answer',
                            json=data, headers=headers, verify=False)
        question_data = res.json()
    else:
        # Get question payload
        data = {
            'template_id': template_id,
            'random_seed': random_seed
        }
        # Get question data
        # es = requests.post('https://www.siyavula.com/api/practice/v1/get-question', json=data, headers=headers, verify=False)
        res = requests.post('https://www.emas/api/practice/v1/get-question',
                            json=data, headers=headers, verify=False)
        question_data = res.json()

    return {
        'token': token,
        'template_id': template_id,
        'random_seed': random_seed,
        'question_html': question_data['question_html']
    }
