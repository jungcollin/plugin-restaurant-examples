#!/usr/bin/env python3
"""
Trace HTML 생성 스크립트.
trace.json 파일을 읽어 독립 실행형 HTML 대시보드를 생성.
"""

import argparse
import json
import os
import sys
from pathlib import Path


def get_template_path() -> Path:
    """템플릿 파일 경로 반환."""
    script_dir = Path(__file__).parent
    template_path = script_dir.parent / "templates" / "trace_template.html"
    return template_path


def load_template() -> str:
    """템플릿 HTML 로드."""
    template_path = get_template_path()
    if not template_path.exists():
        raise FileNotFoundError(f"템플릿 파일을 찾을 수 없습니다: {template_path}")

    with open(template_path, 'r', encoding='utf-8') as f:
        return f.read()


def generate_html(trace_json_path: str, output_path: str = None) -> str:
    """trace.json을 읽어 HTML 대시보드 생성."""

    # trace.json 로드
    with open(trace_json_path, 'r', encoding='utf-8') as f:
        trace_data = json.load(f)

    # 템플릿 로드
    template = load_template()

    # JSON 데이터를 JavaScript에 임베딩
    json_str = json.dumps(trace_data, ensure_ascii=False, indent=2)

    # 자동 로드 스크립트 생성
    auto_load_script = f'''
    // 임베딩된 Trace 데이터 자동 로드
    const EMBEDDED_TRACE_DATA = {json_str};

    // 페이지 로드 시 자동으로 데이터 표시
    document.addEventListener('DOMContentLoaded', function() {{
        // 드롭존 숨기기
        const dropZone = document.getElementById('dropZone');
        if (dropZone) {{
            dropZone.style.display = 'none';
        }}

        // 데이터 로드
        parseTraceJSON(JSON.stringify(EMBEDDED_TRACE_DATA), EMBEDDED_TRACE_DATA.fileName || 'embedded_trace.json');
    }});
'''

    # </script> 태그 직전에 자동 로드 스크립트 삽입
    insert_marker = '</script>\n</body>'
    if insert_marker in template:
        template = template.replace(
            insert_marker,
            f'{auto_load_script}\n</script>\n</body>'
        )
    else:
        # 대체 방법: </body> 직전에 스크립트 추가
        template = template.replace(
            '</body>',
            f'<script>{auto_load_script}</script>\n</body>'
        )

    # 출력 경로 결정
    if output_path is None:
        # trace.json과 같은 디렉토리에 _trace.html로 생성
        base_name = os.path.basename(trace_json_path)
        if base_name.endswith('_trace.json'):
            html_name = base_name.replace('_trace.json', '_trace.html')
        else:
            html_name = base_name.replace('.json', '.html')
        output_path = os.path.join(os.path.dirname(trace_json_path), html_name)

    # HTML 파일 생성
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(template)

    return output_path


def main():
    parser = argparse.ArgumentParser(
        description='Trace JSON을 HTML 대시보드로 변환'
    )
    parser.add_argument(
        'trace_json',
        help='trace.json 파일 경로'
    )
    parser.add_argument(
        '-o', '--output',
        help='출력 HTML 파일 경로 (기본: trace.json과 같은 위치에 .html 확장자로)'
    )

    args = parser.parse_args()

    if not os.path.exists(args.trace_json):
        print(f"❌ 파일을 찾을 수 없습니다: {args.trace_json}", file=sys.stderr)
        sys.exit(1)

    try:
        output_path = generate_html(args.trace_json, args.output)
        print(f"✅ HTML 대시보드 생성 완료: {output_path}")
    except Exception as e:
        print(f"❌ 오류 발생: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
