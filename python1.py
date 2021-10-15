    #현재 작업 위치에서 "python1" 이라는 이름의 폴더와 "python2"라는 폴더가 없다면?
if os.path.exists('python1') == False and os.path.exists('python2') == False:
    # 순환적으로 폴더를 생성함
    # -> exist_ok=True 옵션은 이미 존재하더라도 에러 발생 안함
    os.makedirs('python/test/hello/world', exist_ok=True)
    print('python 폴더와 하위 폴더들을 생성 했습니다.')
    
    # 파일의 이동(같은 위치에서 이름만 변경하는 기능도 겸함)
    # -> 이미 대상이 존재할 경우 에러이므로 사전에 존재여부 검사 필요함
    if os.path.exists('python1') == False:
        shutil.move('python','python1')
        print('python 폴더를 python1로 이동 했습니다.')
        
    # 폴더 복사
    # -> 이미 대상이 존재할 경우 에러이므로 사전에 존재여부 검사 필요함
    if os.path.exists('python2') == False:
        shutil.copytree('python1','python2')
        print('python1폴더를 python2로 복사 했습니다.')
        
# 그렇지 않다면?
else:
    # 비어있지 않은 폴더도 강제 삭제 -> 존재하지 않는 폴더인 경우 에러
    shtil.rmtree('python1')
    shtil.rmtree('python2')
    print('python1, python2 폴더가 삭제되었습니다.')