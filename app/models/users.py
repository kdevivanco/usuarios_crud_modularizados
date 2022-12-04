from app.config.connections import MySQLConnection, connectToMySQL

class User:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    @classmethod
    def get_all(cls):
        
        query = 'SELECT * FROM users'

        results = connectToMySQL('usuarios_cr').query_db('select * from users')
        
        users = []

        for user in results:
            users.append(cls(user))
        
        return users

    @classmethod
    def create_new(cls,form_data):
        query = '''
                INSERT INTO users ( first_name , last_name , email , created_at, updated_at ) 
                VALUES ( %(first_name)s , %(last_name)s , %(email)s , NOW() , NOW() );
                '''

        data = {
                "first_name": form_data["first_name"],
                "last_name" : form_data["last_name"],
                "email" : form_data["email"]
            }
        
        print('Created succesfully')

        return connectToMySQL('usuarios_cr').query_db(query,data)

    @classmethod
    def get_one(cls,id):
        
        query = "SELECT * FROM users WHERE id = %(id)s;"
        data = {
            'id' : id
        }
        results = connectToMySQL('usuarios_cr').query_db(query,data)
        
        print(results)
        
        return results #esto lo saca de la lista para retornar solo el dict.

    @classmethod
    def edit_user(cls,id,form_data):

        query = '''
                UPDATE users  
                SET  first_name  = %(first_name)s,
                last_name  = %(last_name)s,
                email  = %(email)s
                where id = %(id)s
                '''

        data = {
                "first_name": form_data["first_name"],
                "last_name" : form_data["last_name"],
                "email" : form_data["email"],
                "id" : id
            }
        
        results = connectToMySQL('usuarios_cr').query_db(query,data)
        print(data)

        return (data)

    @classmethod
    def delete_user(cls,id):
        query = '''
                DELETE FROM users
                WHERE id = %(id)s;
                '''
        
        data ={
            'id':id
        }

        results = connectToMySQL('usuarios_cr').query_db(query,data)
        print(data)

        return True
