# 카카오 2018 파일명 정렬
import re

def solution(files):
    answer = []
    
    split_files = list()
    for file in files:
        # 영어, -, . 을 묶음으로 전체를 split함
        split_file = re.split(r'([a-zA-Z\-\.\s]+)', file)
        if split_file[0] == '':
            split_file = split_file[1:]
        split_files.append(split_file)

    # split_files 리스트에 인덱스 0과 마지막 인덱스는 빈문자열이 있기 때문에, 정렬은 인덱스 1의 대소문자 구별 X, 인덱스 2를 숫자로 바꿨을 때를 기준으로 한다.
    sorted_split_files = sorted(split_files, key=lambda x: (x[0].lower(), int(x[1])))

    # split한 각 파일들을 다시 문자열로 붙여주면서 answer에 추가함
    for sorted_split_file in sorted_split_files:
        file_str = ''.join(sorted_split_file)
        answer.append(file_str)
    return answer
