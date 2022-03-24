import os

dict_results = {}

def logParser(server):

    # 파일 읽기
    for file in file_list:
        f = open(f'C:/Users/USER/PycharmProjects/test/source/requestLog/{server}/{file}', 'rt', encoding='UTF-8')
        arr_logs = f.readlines()
        f.close()
        print(len(arr_logs))

        for log in arr_logs:
            # org_log = log.replace('\n', '')
            try:
                log = log.split(" ")[4]
                arr_param = log.split("&")
                dict_param = {}

                for params in arr_param:
                    dict_param[params.split('=')[0].lower()] = params.split('=')[1]

                if 'stb_id' in dict_param:
                    stb_id = dict_param['stb_id']

                if stb_id in dict_results:
                    cnt = dict_results[stb_id]
                    dict_results[stb_id] = (cnt + 1)
                else:
                    dict_results[stb_id] = 1

            except Exception as e:
                print(f"parsing error [{e}] - {log}")

    print(f"{server} - {len(dict_results)}")


def test():
    # log = "[2022-03-18 10:00:00] request_nudge_001.INFO: [v524] " \
    #       "/nudge/v1/if-nudge-001?ver=5.3.3&response_format=json&nudge_date=0&menu_ids=menu001,menu008,menu009," \
    #       "menu010,menu013,&stb_id=%7BE6ADA454-3572-11E3-B3DE-39DBAAC4D2B4%7D&model_group=STB&model_name=BID-AT200" \
    #       "&ui_name=BTVANDPV532&if=IF-NUDGE-001 [] []"

    try:
        log = log.split(" ")[4]
        arr_param = log.split("&")
        dict_param = {}

        for params in arr_param:
            dict_param[params.split('=')[0].lower()] = params.split('=')[1]

        if 'stb_id' in dict_param:
            stb_id = dict_param['stb_id']

        if stb_id in dict_results:
            cnt = dict_results[stb_id]
            dict_results[stb_id] = (cnt + 1)
        else:
            dict_results[stb_id] = 1

    except Exception as e:
        print(e)

    print(len(dict_results))


if __name__ == '__main__':
    arr_server = ['171', '172', '173', '174']

    for server in arr_server:
        # 파일 리스트 추출
        file_list = os.listdir(f'C:/Users/USER/PycharmProjects/test/source/requestLog/{server}/')
        logParser(server)

    # test()
