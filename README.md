# News Topic Classifier

한국어 뉴스 문장을 임베딩과 양방향 RNN으로 인코딩하고 주제를 분류하는 수업 프로젝트입니다. 학습 흐름, 모델, 데이터 변환을 news_classifier 패키지로 묶었습니다.

## 코드 구조

| 경로 | 역할 |
|---|---|
| `news_classifier/train.py` | 데이터 로드·토크나이저 선택·학습·평가 |
| `news_classifier/models/` | BiRNN·pooling·분류 헤드 |
| `news_classifier/data/` | pandas와 torchtext 데이터 연결 |
| `news_classifier/preprocessing.py` | 뉴스 문자열 정제·토큰화 |

## 실행

```bash
pip install -e .
python -m news_classifier.train --help
```

PyTorch, legacy torchtext.data, pandas, gensim, KoNLPy/Mecab 등이 필요합니다. 최신 torchtext만 설치하면 실행되는 코드가 아니므로 당시 API를 제공하는 환경을 준비해야 합니다. 데이터와 임베딩은 CLI 경로로 받습니다. Mecab 선택 뒤 다른 조건문이 토크나이저를 지우던 부분을 elif로 수정했습니다.

## Source and license

See [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) for project origins and third-party licenses.
