try:
    # 1. 존재하지 않는 "not-provided.txt" 파일을 읽으려고 시도합니다.
    with open("not-provided.txt", encoding="utf-8") as f:
        print(f.read())
        
except FileNotFoundError:
    # 2. 파일이 없어서 에러(FileNotFoundError)가 발생하면 프로그램이 죽지 않고 이쪽으로 들어와 실행됩니다.
    print("파일 위치를 확인하세요")