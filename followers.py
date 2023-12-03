def facebook_followers():
    from collections import OrderedDict
    followers = OrderedDict()

    while True:
        command = input().split(": ")
        action = command[0]

        if action == "Log out":
            break

        username = command[1]

        if action == "New follower":
            if username not in followers:
                followers[username] = {"likes": 0, "comments": 0}

        elif action == "Like":
            count = int(command[2])
            if username not in followers:
                followers[username] = {"likes": count, "comments": 0}
            else:
                followers[username]["likes"] += count

        elif action == "Comment":
            if username not in followers:
                followers[username] = {"likes": 0, "comments": 1}
            else:
                followers[username]["comments"] += 1

        elif action == "Blocked":
            if username in followers:
                del followers[username]
            else:
                print(f"{username} doesn't exist.")

    print(f"{len(followers)} followers")

    for follower, stats in followers.items():
        print(f"{follower}: {stats['likes'] + stats['comments']}")

facebook_followers()
