def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('get_question', '/')
    config.add_route('get_question_emas', '/emas')
    config.add_route('get_question_mobile', '/mobile')
