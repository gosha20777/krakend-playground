function hello_world( req )
    print('hello world!')
    req:headers('X-from-lua', 'hello world!')
end

function make_req( req )
    print('init http')
    local r = http_response.new('http://static_data:8080/jwk/symmetric.json')
    print('result')
    print(r:statusCode())
    print(r:headers('Content-Type'))
    print(r:body())
    -- custom_error('expect me', 404)
end