# paper1 메인 실행 스크립트 예시
from basic_trader import BasicTrader
from candlestick_analyzer import CandlestickAnalyzer
from sentiment_analyzer import SentimentAnalyzer
import os
import torch
import tqdm
import time
from datetime import datetime

if __name__ == "__main__":
    # 시작 시간 기록
    start_time = time.time()
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] 멀티모달 트레이딩 시뮬레이션 시작")
    
    # GPU 확인 및 사용 설정
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] 사용 가능 디바이스: {device}")
    
    # 설정 정의
    config = {
        'data': {
            'chart_dir': r'D:\drl-candlesticks-trader-main1\paper1\data\chart',  # 차트 데이터 경로
            'news_file': r'D:\drl-candlesticks-trader-main1\paper1\data\news\cryptonews_2021-10-12_2023-12-19.csv',  # 뉴스 데이터 파일
            'timeframes': ['1d', '4h', '1h', '30m', '15m', '5m']  # 분석할 시간프레임 (1d부터 역순)
        },
        'output': {
            'save_dir': r'D:\drl-candlesticks-trader-main1\paper1\results'  # 결과 저장 경로
        },
        # 고급 기술 설정 추가
        'fusion': {
            'type': 'attention'  # 'attention' 또는 'transformer'
        },
        'rl': {
            'use_rl': True,  # 강화학습 사용 여부
            'learning_rate': 0.0003,
            'gamma': 0.99
        },
        'ensemble': {
            'use_ensemble': True,  # 앙상블 방법론 사용 여부
            'timeframe_ensemble_method': 'weighted_average',  # 'voting', 'weighted_average', 'boosting'
            'model_ensemble_method': 'weighted_average'  # 'voting', 'weighted_average', 'stacking'
        }
    }
    
    # 분석기 초기화 (설정 전달)
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] 캔들스틱 분석기 초기화 중...")
    candlestick_analyzer = CandlestickAnalyzer(config)
    
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] 감성 분석기 초기화 중...")
    sentiment_analyzer = SentimentAnalyzer(config)
    
    # 트레이더 초기화 및 실행
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] 트레이더 초기화 중...")
    trader = BasicTrader(candlestick_analyzer, sentiment_analyzer, config)
    
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] 트레이딩 시뮬레이션 실행 중...")
    trader.run()
    
    # 성능 평가 및 결과 저장
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] 성능 평가 중...")
    trader.evaluate_performance()
    
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] 결과 저장 중...")
    trader.save_results()
    
    # 논문 제출용 결과 생성
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] 논문 제출용 결과 생성 중...")
    trader.paper_report_for_submission()
    
    # 실행 시간 계산
    elapsed_time = time.time() - start_time
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] 멀티모달 트레이딩 시뮬레이션 완료! (소요 시간: {elapsed_time:.2f}초)")
