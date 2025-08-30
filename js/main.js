// AI Image Tools - Main JavaScript

// 等待DOM加载完成
document.addEventListener('DOMContentLoaded', function() {
  console.log('AI Image Tools 网站已加载');
  
  // 初始化各个功能
  initSearch();
  initMobileMenu();
  initLazyLoading();
  initToolCards();
  initCategoryFilter();
});

// 1. 搜索功能
function initSearch() {
  const searchInput = document.getElementById('searchInput');
  const searchButton = document.getElementById('searchButton');
  const searchSuggestions = document.getElementById('searchSuggestions');
  
  if (!searchInput) return;
  
  // 搜索建议数据（示例）
  const suggestions = [
    'Midjourney',
    'DALL-E 3',
    'Stable Diffusion',
    'Remove Background',
    'AI Avatar Generator',
    'Image Upscaler',
    'Photo Enhancer'
  ];
  
  // 输入时显示搜索建议
  searchInput.addEventListener('input', function(e) {
    const value = e.target.value.toLowerCase();
    
    if (value.length > 0) {
      const filtered = suggestions.filter(item => 
        item.toLowerCase().includes(value)
      );
      
      showSuggestions(filtered);
    } else {
      hideSuggestions();
    }
  });
  
  // 显示搜索建议
  function showSuggestions(items) {
    if (!searchSuggestions) return;
    
    searchSuggestions.innerHTML = items.map(item => `
      <div class="px-4 py-2 hover:bg-gray-100 cursor-pointer" onclick="selectSuggestion('${item}')">
        ${item}
      </div>
    `).join('');
    
    searchSuggestions.classList.add('active');
  }
  
  // 隐藏搜索建议
  function hideSuggestions() {
    if (searchSuggestions) {
      searchSuggestions.classList.remove('active');
    }
  }
  
  // 点击外部关闭建议
  document.addEventListener('click', function(e) {
    if (!searchInput.contains(e.target)) {
      hideSuggestions();
    }
  });
  
  // 搜索按钮点击
  if (searchButton) {
    searchButton.addEventListener('click', performSearch);
  }
  
  // Enter键搜索
  searchInput.addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
      performSearch();
    }
  });
}

// 选择搜索建议
function selectSuggestion(value) {
  const searchInput = document.getElementById('searchInput');
  if (searchInput) {
    searchInput.value = value;
    document.getElementById('searchSuggestions').classList.remove('active');
    performSearch();
  }
}

// 执行搜索
function performSearch() {
  const searchInput = document.getElementById('searchInput');
  const query = searchInput ? searchInput.value : '';
  
  if (query.trim()) {
    console.log('搜索:', query);
    // 这里后续会跳转到搜索结果页
    // window.location.href = `/search?q=${encodeURIComponent(query)}`;
    alert(`搜索功能开发中...\n搜索词: ${query}`);
  }
}

// 2. 移动端菜单
function initMobileMenu() {
  const menuButton = document.getElementById('mobileMenuButton');
  const mobileMenu = document.getElementById('mobileMenu');
  
  if (menuButton && mobileMenu) {
    menuButton.addEventListener('click', function() {
      mobileMenu.classList.toggle('active');
      document.body.classList.toggle('overflow-hidden');
    });
  }
}

// 3. 图片懒加载
function initLazyLoading() {
  const lazyImages = document.querySelectorAll('img[data-src]');
  
  if ('IntersectionObserver' in window) {
    const imageObserver = new IntersectionObserver((entries, observer) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const img = entry.target;
          img.src = img.dataset.src;
          img.classList.remove('lazy-image');
          img.removeAttribute('data-src');
          observer.unobserve(img);
        }
      });
    });
    
    lazyImages.forEach(img => imageObserver.observe(img));
  } else {
    // 降级方案：直接加载所有图片
    lazyImages.forEach(img => {
      img.src = img.dataset.src;
      img.classList.remove('lazy-image');
    });
  }
}

// 4. 工具卡片交互
function initToolCards() {
  const toolCards = document.querySelectorAll('.tool-card');
  
  toolCards.forEach(card => {
    // 添加点击跳转
    card.addEventListener('click', function(e) {
      // 如果点击的是链接，不处理
      if (e.target.tagName === 'A' || e.target.closest('a')) {
        return;
      }
      
      const toolName = this.dataset.tool;
      if (toolName) {
        // window.location.href = `/tools/${toolName}`;
        console.log('查看工具:', toolName);
      }
    });
  });
}

// 5. 分类筛选
function initCategoryFilter() {
  const categoryButtons = document.querySelectorAll('.category-filter');
  const toolCards = document.querySelectorAll('.tool-card');
  
  categoryButtons.forEach(button => {
    button.addEventListener('click', function() {
      const category = this.dataset.category;
      
      // 更新按钮状态
      categoryButtons.forEach(btn => btn.classList.remove('active'));
      this.classList.add('active');
      
      // 筛选工具卡片
      toolCards.forEach(card => {
        if (category === 'all' || card.dataset.category === category) {
          card.style.display = 'block';
          // 添加淡入动画
          card.style.animation = 'fadeIn 0.5s ease-out';
        } else {
          card.style.display = 'none';
        }
      });
    });
  });
}

// 6. 评分显示
function renderRating(rating, maxRating = 5) {
  const fullStars = Math.floor(rating);
  const hasHalfStar = rating % 1 >= 0.5;
  const emptyStars = maxRating - fullStars - (hasHalfStar ? 1 : 0);
  
  let html = '';
  
  // 满星
  for (let i = 0; i < fullStars; i++) {
    html += '<i class="fas fa-star star"></i>';
  }
  
  // 半星
  if (hasHalfStar) {
    html += '<i class="fas fa-star-half-alt star"></i>';
  }
  
  // 空星
  for (let i = 0; i < emptyStars; i++) {
    html += '<i class="far fa-star star empty"></i>';
  }
  
  return html;
}

// 7. 工具数据加载（未来用于动态加载）
async function loadToolsData() {
  try {
    const response = await fetch('/data/tools.json');
    const tools = await response.json();
    return tools;
  } catch (error) {
    console.error('加载工具数据失败:', error);
    return [];
  }
}

// 8. 滚动到顶部按钮
function initScrollToTop() {
  const scrollButton = document.createElement('button');
  scrollButton.innerHTML = '<i class="fas fa-arrow-up"></i>';
  scrollButton.className = 'fixed bottom-8 right-8 bg-purple-600 text-white w-12 h-12 rounded-full shadow-lg hover:bg-purple-700 transition-all opacity-0 pointer-events-none';
  scrollButton.id = 'scrollToTop';
  document.body.appendChild(scrollButton);
  
  // 显示/隐藏按钮
  window.addEventListener('scroll', function() {
    if (window.pageYOffset > 300) {
      scrollButton.style.opacity = '1';
      scrollButton.style.pointerEvents = 'auto';
    } else {
      scrollButton.style.opacity = '0';
      scrollButton.style.pointerEvents = 'none';
    }
  });
  
  // 点击滚动到顶部
  scrollButton.addEventListener('click', function() {
    window.scrollTo({
      top: 0,
      behavior: 'smooth'
    });
  });
}

// 初始化滚动按钮
initScrollToTop();

// 9. 工具函数：防抖
function debounce(func, wait) {
  let timeout;
  return function executedFunction(...args) {
    const later = () => {
      clearTimeout(timeout);
      func(...args);
    };
    clearTimeout(timeout);
    timeout = setTimeout(later, wait);
  };
}

// 10. 工具函数：节流
function throttle(func, limit) {
  let inThrottle;
  return function(...args) {
    if (!inThrottle) {
      func.apply(this, args);
      inThrottle = true;
      setTimeout(() => inThrottle = false, limit);
    }
  };
}

// 导出函数供其他模块使用
window.AIImageTools = {
  renderRating,
  loadToolsData,
  debounce,
  throttle
};