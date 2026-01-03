def test_radio_filters_chart(dash_duo):
    from main import app

    dash_duo.start_server(app)

    dash_duo.wait_for_element("#heading")

    title = dash_duo.find_element("#heading")
    assert title is not None
    
    dash_duo.wait_for_element("#sales-chart")
    fig = dash_duo.find_element("#sales-chart")
    assert fig is not None
    
    radio_button = dash_duo.find_element("#region")
    assert radio_button is not None