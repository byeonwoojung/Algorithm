def convert(target):
    return min(ord(target)-ord('A'), ord('Z')-ord(target)+1)


def solution(name):
    name_list = list(name)
    name_length = len(name_list)
    move_count = name_length - 1
    
    convert_count = 0
    for i, alp in enumerate(name_list):
        convert_count += convert(alp)
        
        j = i + 1
        # Convert 해야 할 마지막 인덱스 찾기
        while j < name_length and name_list[j] == 'A':
            j += 1
        
        # min(전체 단방향, i까지 갔다가 반대로 돌아서 j까지, 반대로 j까지 갔다가 i로 되돌아오는 것)
        move_count = min(move_count, i * 2 + (name_length-j), (name_length-j)*2 + i)
        
    return convert_count + move_count