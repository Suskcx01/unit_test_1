class Men:
    name = []

    def set_name(self, user_name):
        self.name.append(user_name)
        return len(self.name) - 1

    def get_name(self, user_id):
        if user_id >= len(self.name):
            return 'There is no such user'
        else:
            return self.name[user_id]


if __name__ == '__main__':
    men = Men()
    print('User Pete has been added with id ', men.set_name('Pete'))
    print('User associated with id 0 is ', men.get_name(0))