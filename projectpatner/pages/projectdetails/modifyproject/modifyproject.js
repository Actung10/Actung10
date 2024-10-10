// pages/projectdetails/modifyproject/modifyproject.js
Page({
  data: {
    projectId: null, // 当前编辑的项目ID
    projectName: '', // 项目名称
    projectIntroduction: '', // 项目简介
    projectContent: '', // 项目内容
    mentor: '', // 指导教师
    projectMembers: '', // 项目人数
    statusOptions: ['招募人员', '进行中', '已完成'], // 状态选项
    statusIndex: 0, // 默认选中第一个状态
  },
  onLoad: function(options) {
    // 获取传递过来的项目ID
    this.setData({
      projectId: parseInt(options.projectId, 10)
    });
    this.loadProjectDetails();
  },
  
  // onShow 方法
  onShow: function() {
    // 每次显示页面时重新加载项目详情，确保数据是最新的
    this.loadProjectDetails();
  },
  
  // 加载项目详情的方法
  loadProjectDetails: function() {
    const projectId = this.data.projectId;
    const app = getApp();
    const project = app.globalData.projects.find(p => p.id === projectId);
  
    if (project) {
      // 设置表单数据
      this.setData({
        projectName: project.name,
        projectIntroduction: project.introduction,
        projectContent: project.content,
        mentor: project.mentor,
        projectMembers: project.totalMembers.toString(),
        statusIndex: this.data.statusOptions.indexOf(project.status), // 设置正确的状态索引
      });
    } else {
      // 如果没有找到项目，显示错误信息并返回上一页
      wx.showToast({
        title: '项目不存在',
        icon: 'none',
      });
      setTimeout(() => {
        wx.navigateBack({
          delta: 1,
        });
      }, 1500); // 延迟1.5秒后返回上一页
    }
  },

  inputProjectName: function(e) {
    this.setData({
      projectName: e.detail.value
    });
  },
  inputProjectIntroduction: function(e) {
    this.setData({
      projectIntroduction: e.detail.value
    });
  },
  inputProjectContent: function(e) {
    this.setData({
      projectContent: e.detail.value
    });
  },
  inputMentor: function(e) {
    this.setData({
      mentor: e.detail.value
    });
  },
  inputProjectMembers: function(e) {
    this.setData({
      projectMembers: e.detail.value
    });
  },

  onStatusChange: function(e) {
    this.setData({
      statusIndex: e.detail.value
    });
  },

  goBack() {
    wx.navigateBack({
      delta: 1
    });
  },

  saveProject: function() {
    const app = getApp();
    const index = app.globalData.projects.findIndex(p => p.id === this.data.projectId);
    if (index !== -1) {
      // 更新项目信息
      app.globalData.projects[index] = {
        id: this.data.projectId,
        name: this.data.projectName,
        introduction: this.data.projectIntroduction,
        content: this.data.projectContent,
        mentor: this.data.mentor,
        totalMembers: parseInt(this.data.projectMembers, 10),
        status: this.data.statusOptions[this.data.statusIndex], // 确保状态也被更新
      };
      // 保存全局数据到本地存储
      wx.setStorageSync('projects', app.globalData.projects);
      wx.showToast({
        title: '项目修改成功',
        icon: 'success',
      });
      setTimeout(() => {
        wx.navigateBack({
          delta: 1,
        });
      }, 1500); // 延迟1.5秒后返回上一页
    } else {
      wx.showToast({
        title: '项目不存在',
        icon: 'none',
      });
    }
  },
  
});