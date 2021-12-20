const { Component, mount } = owl;
const { xml } = owl.tags;
const { whenReady } = owl.utils;
const { useRef, useState } = owl.hooks;

const TASK_TEMPLATE = xml`<div class="task" t-att-class="props.task.isCompleted ? 'done' : ''">
                            <input type="checkbox" t-att-checked="props.task.isCompleted" t-on-click="toggleTask"/>
                            <span><t t-esc="props.task.title"/></span>
                            <span class="delete" t-on-click="deleteTask">🗑</span>
                          </div>`;

class Task extends Component {
  static template = TASK_TEMPLATE;
  static props = ["task"];

  toggleTask() {
    this.trigger('toggle-task', {id: this.props.task.id});
  }

  deleteTask() {
    this.trigger('delete-task', {id: this.props.task.id});
  }

}

const APP_TEMPLATE = xml`<div class="todo-app">
                          <input placeholder="Enter a new task" t-on-keyup="addTask" t-ref="add-input"/>
                          <div class="task-list" t-on-toggle-task="toggleTask" t-on-delete-task="deleteTask">
                            <t t-foreach="tasks" t-as="task" t-key="task.id">
                              <Task task="task"/>
                            </t>
                          </div>
                        </div>`;

class App extends Component {
  // App.template = xml`<div>todo app</div>`;
  static template = APP_TEMPLATE;
  static components = { Task };

  inputRef = useRef("add-input");
  tasks = useState([]);
  nextId = 1;

  mounted() {
    this.inputRef.el.focus();
  }

  addTask(ev) {
    if(ev.keyCode === 13) {
      const title = ev.target.value.trim();
      ev.target.value="";
      // console.log(title);
      if(title) {
        const newTask = {
          id: this.nextId++,
          title: title,
          isComplated: false
        };
        this.tasks.push(newTask);
      }
    }
  }

  toggleTask(ev) {
    const task = this.tasks.find(t => t.id === ev.detail.id);
    task.isComplated = !task.isComplated;
  }

  deleteTask(ev) {
    const index = this.tasks.findIndex( (t) => t.id == ev.detail.id);
    this.tasks.splice(index,1);
  }
}



function setup() {
  owl.config.mode = "dev";
  mount(App, { target : document.body});
}

whenReady(setup);