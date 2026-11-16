# 위치 확인 코드 — 그대로 실행합니다
import os                                         # 폴더 · 파일을 다루는 도구
import sys                                        # 지금 실행 중인 파이썬의 정보를 주는 도구

print("Python 파일이 실행되는 폴더:", os.getcwd())          # 오늘 만드는 파일이 생기는 폴더
print("지금 쓰는 파이썬     :", sys.executable)         # 경로에 가상환경 폴더 이름이 보여야 한다

if os.path.basename(os.getcwd()) == "agent_core":  # 지금 폴더 이름이 agent_core 이면
    print("준비 완료")                              # 자리가 맞다
else:                                             # 다른 폴더이면
    print("이 Python 파일을 security-agent-toolkit 폴더 안의 agent_core 폴더로 옮긴 뒤 다시 엽니다")
