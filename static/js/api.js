/**
 * api.js — Utilidades compartidas para la API del sistema de gestión académica.
 * Se usa desde todos los templates HTML para autenticación y llamadas a la API.
 */

const API_BASE = window.location.origin + '/api';

const Auth = {
    setTokens(tokens) {
        localStorage.setItem('access_token', tokens.access);
        localStorage.setItem('refresh_token', tokens.refresh);
    },
    setUser(user) {
        localStorage.setItem('user', JSON.stringify(user));
    },
    getAccessToken() {
        return localStorage.getItem('access_token');
    },
    getRefreshToken() {
        return localStorage.getItem('refresh_token');
    },
    getUser() {
        const u = localStorage.getItem('user');
        return u ? JSON.parse(u) : null;
    },
    clear() {
        localStorage.removeItem('access_token');
        localStorage.removeItem('refresh_token');
        localStorage.removeItem('user');
    },
    isLoggedIn() {
        return !!this.getAccessToken();
    },
    requireAuth() {
        if (!this.isLoggedIn()) {
            window.location.href = '/';
            return false;
        }
        return true;
    },
    async logout() {
        try {
            await apiFetch('/auth/logout/', {
                method: 'POST',
                body: JSON.stringify({ refresh: this.getRefreshToken() })
            });
        } catch (e) { /* ignore */ }
        this.clear();
        window.location.href = '/';
    },
    redirectByRole(rol) {
        const routes = {
            'ADMIN': '/dashboard/admin/',
            'PROFESOR': '/dashboard/profesor/cursos/',
            'ESTUDIANTE': '/dashboard/estudiante/cursos/'
        };
        window.location.href = routes[rol] || '/';
    }
};

/**
 * Fetch wrapper que incluye el token JWT automáticamente.
 */
async function apiFetch(endpoint, options = {}) {
    const token = Auth.getAccessToken();
    const headers = {
        ...(token ? { 'Authorization': `Bearer ${token}` } : {}),
        ...(options.headers || {})
    };

    // Only add application/json if we are not sending FormData
    if (!(options.body instanceof FormData)) {
        headers['Content-Type'] = headers['Content-Type'] || 'application/json';
    }

    const res = await fetch(`${API_BASE}${endpoint}`, {
        ...options,
        headers
    });

    // Si el token expiró, redirigir al login
    if (res.status === 401) {
        Auth.clear();
        window.location.href = '/';
        return null;
    }

    return res;
}

/**
 * Helper para GET con JSON parsing.
 */
async function apiGet(endpoint) {
    const res = await apiFetch(endpoint);
    if (!res) return null;
    return await res.json();
}

/**
 * Helper para POST con JSON body.
 */
async function apiPost(endpoint, data) {
    const res = await apiFetch(endpoint, {
        method: 'POST',
        body: JSON.stringify(data)
    });
    if (!res) return null;
    return { ok: res.ok, status: res.status, data: await res.json() };
}

/**
 * Helper para PUT con JSON body.
 */
async function apiPut(endpoint, data) {
    const res = await apiFetch(endpoint, {
        method: 'PUT',
        body: JSON.stringify(data)
    });
    if (!res) return null;
    return { ok: res.ok, status: res.status, data: await res.json() };
}

/**
 * Helper para PATCH con JSON body.
 */
async function apiPatch(endpoint, data) {
    const res = await apiFetch(endpoint, {
        method: 'PATCH',
        body: JSON.stringify(data)
    });
    if (!res) return null;
    return { ok: res.ok, status: res.status, data: await res.json() };
}

/**
 * Helper para DELETE.
 */
async function apiDelete(endpoint) {
    const res = await apiFetch(endpoint, { method: 'DELETE' });
    if (!res) return null;
    return { ok: res.ok, status: res.status };
}

/**
 * Wires up all Sign Out links/buttons in the page.
 */
function wireLogout() {
    document.querySelectorAll('a, button').forEach(el => {
        if (el.textContent.trim() === 'Sign Out') {
            el.addEventListener('click', (e) => {
                e.preventDefault();
                Auth.logout();
            });
        }
    });
}

/**
 * Shows a toast notification.
 */
function showToast(message, type = 'success') {
    const toast = document.createElement('div');
    const colors = {
        success: 'bg-primary text-white',
        error: 'bg-error text-on-error',
        info: 'bg-surface-tint text-white'
    };
    toast.className = `fixed bottom-6 right-6 ${colors[type] || colors.info} px-6 py-3 rounded-lg shadow-2xl z-[100] font-semibold text-sm transition-all transform translate-y-0 opacity-100`;
    toast.textContent = message;
    document.body.appendChild(toast);
    setTimeout(() => {
        toast.style.opacity = '0';
        toast.style.transform = 'translateY(10px)';
        setTimeout(() => toast.remove(), 300);
    }, 3000);
}
