#!/usr/bin/env python3
"""
Trace 초기화 스크립트.
타임스탬프 기반 스텁 파일(trace.json, 결과물.md)을 생성.
"""

import argparse
import json
import os
import re
from datetime import datetime


def sanitize_filename(text: str, max_length: int = 50) -> str:
    """파일명에 사용할 수 있도록 텍스트 정리."""
    # 공백을 언더스코어로
    text = text.replace(" ", "_")
    # 파일명에 부적합한 문자 제거
    text = re.sub(r'[<>:"/\\|?*]', '', text)
    # 연속 언더스코어 정리
    text = re.sub(r'_+', '_', text)
    # 앞뒤 언더스코어 제거
    text = text.strip('_')
    # 길이 제한
    return text[:max_length]


def create_trace_stub(timestamp: str, summary: str, output_dir: str) -> dict:
    """trace.json 스텁 파일 생성."""
    filename = f"{timestamp}_{summary}_trace.json"
    filepath = os.path.join(output_dir, filename)

    start_time = datetime.now().strftime("%Y-%m-%d %H:%M")

    trace_data = {
        "schemaVersion": "1.0",
        "fileName": filename,
        "runId": timestamp,
        "startTime": start_time,
        "summary": "TODO: 요청 요약 작성",
        "status": "unknown",
        "groupRelation": {
            "text": "TODO: 그룹 관계 설명",
            "type": "sequential"
        },
        "groups": [
            {
                "number": "1",
                "type": "sequential",
                "info": "TODO: 그룹 설명",
                "tasks": [
                    {
                        "name": "TODO: 작업명",
                        "agent": "main",
                        "status": "pending"
                    }
                ]
            }
        ],
        "skills": [],
        "artifacts": [
            {
                "name": f"{timestamp}_{summary}.md",
                "type": "MD"
            }
        ]
    }

    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(trace_data, f, ensure_ascii=False, indent=2)

    return {"path": filepath, "filename": filename}


def create_result_stub(timestamp: str, summary: str, output_dir: str) -> dict:
    """결과물 .md 스텁 파일 생성."""
    filename = f"{timestamp}_{summary}.md"
    filepath = os.path.join(output_dir, filename)

    content = f"""# {summary}

> Run ID: {timestamp}
> 생성 시각: {datetime.now().strftime("%Y-%m-%d %H:%M")}

---

TODO: 결과물 내용 작성

"""

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    return {"path": filepath, "filename": filename}


def main():
    parser = argparse.ArgumentParser(description='Trace 초기화: 스텁 파일 생성')
    parser.add_argument('summary', help='요청 요약 (파일명에 사용)')
    parser.add_argument('--output-dir', '-o', default='.', help='출력 디렉토리 (기본: 현재 디렉토리)')

    args = parser.parse_args()

    # 타임스탬프 생성
    timestamp = datetime.now().strftime("%Y%m%d%H%M")

    # 요약 정리 (파일명용)
    summary_clean = sanitize_filename(args.summary)

    # 출력 디렉토리 확인/생성
    output_dir = os.path.abspath(args.output_dir)
    os.makedirs(output_dir, exist_ok=True)

    # 스텁 파일 생성
    trace_info = create_trace_stub(timestamp, summary_clean, output_dir)
    result_info = create_result_stub(timestamp, summary_clean, output_dir)

    # 결과 출력
    print(f"=== Trace 초기화 완료 ===")
    print(f"Run ID (T): {timestamp}")
    print(f"Summary (S): {summary_clean}")
    print(f"Output Dir: {output_dir}")
    print(f"")
    print(f"생성된 파일:")
    print(f"  - {trace_info['filename']}")
    print(f"  - {result_info['filename']}")
    print(f"")
    print(f"다음 단계: 작업 수행 후 스텁 파일의 TODO 항목을 채우세요.")


if __name__ == "__main__":
    main()
