// app.js
App({
  globalData: {
    theme: 'light', // dark
    mode: '', // 模式(care：关怀模式)
    users: [
      {
        id: 1,
        username: '111111',
        password: '111111',
        name: '乙同学',
        signature: '这是一条个签',
        avatarUrl: '/static/tabbar/me.png',
        joinedProjects: [2,3], // 用户参与的项目
        createdProjects: [1] // 用户创建的项目
      }
      // 可以添加更多用户信息
    ],
    currentUser: null, // 当前登录的用户信息
    projects: [
      // 所有项目的信息
      { id: 1, name: '自动驾驶技术', members: ['乙同学', '周同学'], currentMembersCount: 2, totalMembers: 5, initiator: '乙同学', mentor: '丙老师', introduction: '研究和开发自动驾驶技术', content: '本项目致力于研究自动驾驶技术，包括感知系统、决策算法和控制策略，目标是提高自动驾驶系统的安全性和可靠性。', status: '招募人员' },
      { id: 2, name: '深度学习探索', members: ['甲同学', '张同学', '李同学','乙同学'], currentMembersCount: 4, totalMembers: 5, initiator: '甲同学', mentor: '丙老师', introduction: '探索深度学习在图像识别中的应用', content: '本项目旨在通过深度学习技术，提高图像识别的准确率，研究如何利用神经网络模型来分析和识别图像中的对象。', status: '招募人员' },
      { id: 3, name: '游戏世界构建', members: ['赵同学','陈同学', '林同学', '李同学','乙同学'], currentMembersCount: 5, totalMembers: 8, initiator: '赵同学', mentor: '刘老师', introduction: '构建一个虚拟的游戏世界', content: '本项目的目标是设计和开发一个虚拟的游戏世界，包括角色设计、故事情节和游戏机制。', status: '招募人员' },
      { id: 4, name: '智能机器人研发', members: ['吴同学', '郑同学'], currentMembersCount: 2, totalMembers: 6, initiator: '吴同学', mentor: '孙老师', introduction: '研发一款能够执行家务的智能机器人', content: '本项目的目标是设计和开发一款智能机器人，它能够自动执行家务任务，如扫地、洗碗和洗衣服。', status: '招募人员' },
      { id: 5, name: '大数据分析', members: ['冯同学', '陈同学'], currentMembersCount: 2, totalMembers: 7, initiator: '冯同学', mentor: '周老师', introduction: '分析和处理大数据', content: '本项目旨在通过大数据分析技术，提取有价值的信息，为决策提供支持。', status: '招募人员' },
      { id: 6, name: '物联网应用开发', members: ['褚同学', '卫同学'], currentMembersCount: 2, totalMembers: 4, initiator: '褚同学', mentor: '沈老师', introduction: '开发物联网应用', content: '本项目的目标是开发物联网应用，实现设备的智能控制和数据收集。', status: '招募人员' },
      { id: 7, name: '区块链技术研究', members: ['韩同学', '杨同学'], currentMembersCount: 2, totalMembers: 5, initiator: '韩同学', mentor: '秦老师', introduction: '研究区块链技术', content: '本项目致力于研究区块链技术的原理和应用，探索其在金融、供应链等领域的潜力。', status: '招募人员' },
      { id: 8, name: '虚拟现实体验', members: ['郭同学', '曹同学'], currentMembersCount: 2, totalMembers: 6, initiator: '郭同学', mentor: '何老师', introduction: '开发虚拟现实体验', content: '本项目的目标是开发虚拟现实体验，提供沉浸式的娱乐和教育体验。', status: '招募人员' }
    ]
  },
  onLaunch: function() {
    // 小程序启动时执行的初始化操作
    this.initData();
  },
  initData: function() {
    // 确保初始数据已定义
    const users = this.globalData.users || [];
    const currentUser = wx.getStorageSync('currentUser') || (users.length > 0 ? users[0] : null);
    const projects = this.globalData.projects || [];
  
    // 如果本地存储中没有用户信息，则设置初始用户信息
    if (!wx.getStorageSync('users') || !wx.getStorageSync('users').length) {
      wx.setStorageSync('users', users);
    }
  
    // 如果本地存储中没有当前用户，则设置初始当前用户
    if (!currentUser) {
      wx.setStorageSync('currentUser', users[0]);
    }
  
    // 如果本地存储中没有项目信息，则设置初始项目信息
    if (!wx.getStorageSync('projects') || !wx.getStorageSync('projects').length) {
      wx.setStorageSync('projects', projects);
    }
  
    // 更新全局数据
    this.globalData.users = wx.getStorageSync('users') || users;
    this.globalData.currentUser = wx.getStorageSync('currentUser') || currentUser;
    this.globalData.projects = wx.getStorageSync('projects') || projects;
  },
})
