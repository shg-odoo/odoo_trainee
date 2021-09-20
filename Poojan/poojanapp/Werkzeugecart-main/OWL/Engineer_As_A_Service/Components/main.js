const { Component, mount, Store, qweb } = owl;
const { xml } = owl.tags;
const { EventBus } = owl.core;
const { RouteComponent } = owl.router
const { whenReady } = owl.utils;
const { useRef, useDispatch, useState, useStore } = owl.hooks;

import { HeaderComponent } from "./include/HeaderComponent.js";
import { FooterComponent } from "./include/FooterComponent.js";

import { Home } from "./HomeComponent.js";
import { Login } from "./LoginComponent.js";
import { Signup } from "./signUpComponent.js";
// engineer
import { signup_engineer } from "./signup_engineer.js";
import { HomeEngineer } from "./engineer/HomeEngineer.js";
import { Jobs } from "./engineer/Jobs.js";
import { Engineer_profile } from "./engineer/Engineer_profile.js";
import { New_Jobs_engineer } from "./engineer/New_Jobs_engineer.js";
import { view_jobs_detail } from "./engineer/view_jobs_detail.js";

// Client
import { HomeClient } from "./client/HomeClient.js";
import { client_Engineer_list } from "./client/client_Engineer_list.js";
import { Orders } from "./client/Orders.js";
import { client_profile } from "./client/client_profile.js";
import { view_engineer_detail } from "./client/view_engineer_detail.js";
import { view_orders_detail } from "./client/view_orders_detail.js";



class home extends Component {
   static components = {RouteComponent,HeaderComponent,FooterComponent};

   static template = xml`<div>
        <div>
          <HeaderComponent/>
          <RouteComponent/>
          <FooterComponent/> 
        </div>
    </div>`;

    async willStart() {
        
        // const cookieArr = document.cookie.split(";");
        //     for(var i = 0; i < cookieArr.length; i++) {
        //         var cookiePair = cookieArr[i].split("=");
        //             const res = decodeURIComponent(cookiePair[1]);

        //         const xhr = new window.XMLHttpRequest();
        //         xhr.open('POST', '/do_fetch');
        //         xhr.send(JSON.stringify({'session_id': res}));
        //         xhr.onload = async () => {
        //             const response = JSON.parse(xhr.response);
        //             console.log(response.fetch_detail);
        //             this.env.bus.trigger('client_engineer', {valid: response.fetch_detail});
                    
        //         }
        //     }
    }
}       


const ROUTES = [
    // Before Login
    { name: "home", path: "/", component: Home },
    { name: "signup", path: "/signup", component: Signup },
    { name: "signup_engineer", path: "/signupEngineer", component: signup_engineer },
    { name: "login", path: "/login", component: Login },
    // engineer
    { name: "HomeEngineer", path: "/homee", component: HomeEngineer },
    { name: "jobs", path: "/jobs", component: Jobs },
    { name: "Engineer_profile", path: "/profile", component: Engineer_profile },
    { name: "new_jobs_engineer", path: "/new_jobs", component: New_Jobs_engineer },
    { name: "view_jobs_detail", path: "/view_jobs_detail", component: view_jobs_detail },


    // client
    { name: "HomeClient", path: "/home", component: HomeClient },
    { name: "client_Engineer_list", path: "/engineerslist", component: client_Engineer_list },
    { name: "Orders", path: "/orders", component: Orders },
    { name: "client_profile", path: "/profilee", component: client_profile },
    { name: "view_engineer_detail", path: "/view_engineer_detail", component: view_engineer_detail },
    { name: "view_orders_detail", path: "/view_orders_detail", component: view_orders_detail },
];



function makeEnvironment() {
    const env = { qweb };   
    const router = new owl.router.Router(env, ROUTES);
    env.router.start();
    env.bus = new EventBus();
    return env;
}


home.env = makeEnvironment()

function setup() {
    const app = new home();
/*    app.env.router.navigate({to: 'signup'});
*/    app.mount(document.body);
}

whenReady(setup);