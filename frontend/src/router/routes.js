
function checkIfLogged() {
  const userid = localStorage.getItem("userid");
  if (userid == null) return '/signin';
}

const routes = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/Index.vue') },
      { path: 'signin', name: 'signin', component: () => import('pages/SignIn.vue') },
      { path: 'register', name: 'register', component: () => import('pages/Register.vue') },
      {
        path: '/dashboard',
        name: 'dashboard',
        component: () => import('pages/Dashboard.vue'),
        beforeEnter: [checkIfLogged], 
      }
    ]
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: '/:catchAll(.*)*',
    component: () => import('pages/Error404.vue')
  }
]

export default routes
