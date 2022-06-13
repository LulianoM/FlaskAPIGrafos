import pandas as pd

class GrafosDomain:

    def NameInNodes(data, name):
        if name in data.columns.to_list():
            return True
        else:
            False

    def SearchAllFriends(data, name):
        return {name: data[name].dropna().tolist()}

    def SearchFriendsByOtherFriend(data, name):
        friendsList = GrafosDomain.SearchAllFriends(data, name)
        friendsOutMyList = []

        for friendName in friendsList[name]:
            otherFriendsList = GrafosDomain.SearchAllFriends(data, friendName) 
            for otherFriend in otherFriendsList[friendName]:
                if otherFriend not in friendsList[name] and otherFriend != name:
                    friendsOutMyList.append(otherFriend)
        return {name: friendsOutMyList}
