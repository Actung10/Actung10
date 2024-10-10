// pages/project/project.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    createdProjects: [], // 我创建的项目列表
    joinedProjects: [],  // 我参加的项目列表
    showCreated: true,    // 是否显示我创建的项目
    showJoined: true,     // 是否显示我参加的项目
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad(options) {
    const app = getApp();
    const currentUser = app.globalData.users.find(user => user.id === 1); // 假设你要加载的用户ID为1
    const createdProjects = this.initProjects(currentUser.createdProjects);
    const joinedProjects = this.initProjects(currentUser.joinedProjects, 'joined');

    this.setData({
      createdProjects,
      joinedProjects,
    });
  },

  // 生命周期函数--监听页面显示
  onShow: function() {
    const app = getApp();
    const currentUser = app.globalData.users.find(user => user.id === 1); // 假设你要加载的用户ID为1
    const createdProjects = this.initProjects(currentUser.createdProjects);
    const joinedProjects = this.initProjects(currentUser.joinedProjects);
    this.setData({
      createdProjects,
      joinedProjects
    });
  },

  initProjects: function(projectIds, type) {
    const app = getApp();
    const allProjects = app.globalData.projects;
    const projects = projectIds.map(id => allProjects.find(project => project.id === id));
    return projects;
  },

  toggleProjects: function(e) {
    const type = e.currentTarget.dataset.type;
    if (type === 'created') {
      this.setData({
        showCreated: !this.data.showCreated,
      });
    } else {
      this.setData({
        showJoined: !this.data.showJoined
      });
    }
  },
  createnewProject() {
    // 跳转到另一个页面的函数
    wx.navigateTo({
      url: '/pages/project/create/create'
    });
  },
})