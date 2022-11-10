from app import app, db, mail, mqtt, login_manager

if __name__=='__main__':
    db.create_all()
    app.run()
    mail.init_app(app)
    mqtt.init_app(app)
    login_manager.init_app(app)
    
   
    

