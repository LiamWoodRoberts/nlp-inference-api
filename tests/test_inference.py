test_phrases = ["Joe Biden is the president of the United States"]
api_version = "1.0"


def test_post_ngrams(test_app):
    payload = {"responses": test_phrases}
    response = test_app.post(
        f"/api/v{api_version}/inference/ngrams", json=payload
    )
    assert response.status_code == 200
