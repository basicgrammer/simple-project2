from django.db import transaction
from platform_app.models import *
import copy

class PlatService :

    @transaction.atomic    
    def insert_item_data(parser_data:dict) -> "Reponse Code, Message, Response Data" :

        ''' 
        ## 동작 기능 설명
        - 3 개의 ProductOption 을 생성 후 연결
        - 이미 존재하던 1개의 Tag(name: ExistTag) 를 연결
        - 1개의 Tag 를 생성(name: NewTag) 후 연결
        '''     

        ## 3개의 ProductOption 생성 후 연결 --> 만약 전제조건으로 해당하는 테이블이 없다고 하면 로직 분기가 2가지로 나뉘어짐
        # 1. 해당 테이블에서 필터링되는 데이터가 없는 경우 Product 테이블에서 신규 데이터를 생성 후 3개의 ProductOption 테이블에 insert할 데이터 생성 및 연결
        # 2. 해당 테이블에서 필터링되는 데이터가 있는 경우 3개의 ProductOption 생성 및 연결

        product_query = Product.objects.filter(name = parser_data['name'])

        query_set = ProductOption()

        bulk_query = []        
        
        # 1. 3개의 ProductOption 테이블 관련 데이터 생성 및 연결 과정 
        if product_query.exists() :

            ## 이미 해당하는 조건에 부합하는 쿼리가 존재하므로 생성할 필요 없이 연결하여 ProductionOption 테이블에 데이터를 insert함
            ## 비교 조건은 pk가 존재하지 않으므로 name으로 함

            

            for index in parser_data['option_set'] :

                query_set.product = product_query[0]
                query_set.name = index['name']
                query_set.price = index['price']

                ## 메모리 주소가 복사되어 기존 배열 데이터가 동일하게 변하는 문제로 deepcopy를 활용해서 리스트에 저장되는 원본 데이터를 유지하고자 한다.
                bulk_query.append(copy.deepcopy(query_set))
        
        else :

            query_set = Product()
            query_set1.name = parser_data['name']
            query_set1.save()

            for index in parser_data['option_set'] :

                query_set.product = query_set1
                query_set.name = index['name']
                query_set.price = index['price']

                bulk_query.append(copy.deepcopy(query_set))

        ## Bulk 과정을 통해 한꺼번에 1단계 데이터를 insert 처리함
        ProductOption.objects.bulk_create(bulk_query)


        # 2~3단계 : tag_set 수정 및 생성 작업


        for index in parser_data['tag_set'] :

            tag_query = Tag.objects.filter(id = index.get('pk'))

            if tag_query.exists() :

                tag_query[0].name = index['name']
                tag_query[0].save()

            else : 
                
                check = Tag.objects.filter(name = index['name'])
                
                if check.exists() :

                    pass

                else :

                    create = Tag.objects.create(name = index['name'])
                    create.save()

        # 응답 데이터 반환

        res_code = 200
        # response_data = dict()

        response_data = parser_data

        header_data = Product.objects.get(name = parser_data['name'])
        option_set_data = []
        tag_set_data = []

        # print(combine_data1.id)
        # print(combine_data1.name)

        # print(parser_data)
        # response_data['pk'] = combine_data1.id
        # response_data['name'] = combine_data1.name


        
        for index in response_data['option_set'] :

            option_query = ProductOption.objects.get(name = index['name'])


            ## 응답 데이터를 위한 재조합 과정 수행
            tmp1 = index['name']
            tmp2 = index['price']
            index['pk'] = option_query.id
            index.pop('name')
            index.pop('price')
            index['name'] = tmp1
            index['price'] = tmp2

        option_set_data = response_data['option_set']
            

        for index in response_data['tag_set'] :

            tag_query = Tag.objects.get(name = index['name'])
            
            ## 응답 데이터를 위한 재조합 과정 수행
            index['pk'] = tag_query.id
            tmp1 = index['name']
            index.pop('name')
            index['name'] = tmp1

        tag_set_data = response_data['tag_set']

        return res_code, header_data, option_set_data, tag_set_data



        # response_data['pk'] = combine_data1.id
        # response_data['name'] = combine_data1.name
        # response_data['option_set'] = ProductOption.objects.filter(product_id = combine_data1.id)

        # res_data = ProductOption.objects.select_related('product').filter(product_id = product_query[0].id)


        # for item in res_data :

        #     print(item.name)
        #     print(item.price)
        #     print(item.product.name)

        




        #     ## 존재하지 않으므로

        # query_set1 = Product() 

        # query_set1.name = parser_data['name']

        # query_set1.save()



        # product_check = Product.objects.filter(id = query_set1.id)


        # query_set = ProductOption()

        # ## bulk create 작업을 위해 한곳에 모아놓기 위해 선언함

        # bulk_query = []

        # ## bulk create 
        # if product_check.exists() :

        #     for index in parser_data['option_set'] :

        #         query_set.product = product_check[0]
        #         query_set.name = index['name']
        #         query_set.price = index['price']
                
        #         bulk_query.append(query_set)

        #     ## bulk create 구성에서는 한개의 insert문이 하나의 트랜잭션으로 묶여서 실행되므로, insert 실패시 자동으로 롤백됨
        #     ProductOption.objects.bulk_create(bulk_query)


        #     for index in parser_data['tag_set'] :

        #         print(index)

        #         product_query = Product.objects.filter(id = index['pk'])

        #         # print(index.get('pk'))
        #         # print(index['pk'].get())

                
        #         # ## 존재하면 None이 아닌 해당 키에 대응되는 값을 받음
        #         if index.get('pk') is not None and product_query.exists() :

        #             # product_query[0].tag_set.set(index['name'])

        #             product_tag_set.objects.create()
                    

        #         # ## 없는 경우 자동으로 pk 2번의 값을 이어서 선택
        #         else :

        #             pass



                    
                    



                    


