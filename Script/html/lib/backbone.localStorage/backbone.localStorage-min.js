/**
 * Backbone localStorage Adapter
 * Version 1.1.13
 *
 * https://github.com/jeromegn/Backbone.localStorage
 */
(function(a, b) {
    typeof exports == "object" && typeof require == "function" ? module.exports = b(require("backbone")) : typeof define == "function" && define.amd ? define(["backbone"], function(c) {
        return b(c || a.Backbone)
    }) : b(Backbone)
})(this, function(a) {
    function b() {
        return ((1 + Math.random()) * 65536 | 0).toString(16).substring(1)
    }
    function c() {
        return b() + b() + "-" + b() + "-" + b() + "-" + b() + "-" + b() + b() + b()
    }
    function d(a) {
        return a === Object(a)
    }
    function e(a, b) {
        var c = a.length;
        while (c--)
            if (a[c] === b)
                return !0;
        return !1
    }
    function f(a, b) {
        for (var c in b)
            a[c] = b[c];
        return a
    }
    return a.LocalStorage = window.Store = function(a, b) {
        if (!this.localStorage)
            throw "Backbone.localStorage: Environment does not support localStorage.";
        this.name = a, this.serializer = b || {
            serialize: function(a) {
                return d(a) ? JSON.stringify(a) : a
            },
            deserialize: function(a) {
                return a && JSON.parse(a)
            }
        };
        var c = this.localStorage().getItem(this.name);
        this.records = c && c.split(",") || []
    }, f(a.LocalStorage.prototype, {
        save: function() {
            this.localStorage().setItem(this.name, this.records.join(","))
        },
        create: function(a) {
            return a.id || (a.id = c(), a.set(a.idAttribute, a.id)), this.localStorage().setItem(this._itemName(a.id), this.serializer.serialize(a)), this.records.push(a.id.toString()), this.save(), this.find(a)!==!1
        },
        update: function(a) {
            this.localStorage().setItem(this._itemName(a.id), this.serializer.serialize(a));
            var b = a.id.toString();
            return e(this.records, b) || (this.records.push(b), this.save()), this.find(a)!==!1
        },
        find: function(a) {
            return this.serializer.deserialize(this.localStorage().getItem(this._itemName(a.id)))
        },
        findAll: function() {
            var a = [];
            for (var b = 0, c, d; b < this.records.length; b++)
                c = this.records[b], d = this.serializer.deserialize(this.localStorage().getItem(this._itemName(c))), d != null && a.push(d);
            return a
        },
        destroy: function(a) {
            this.localStorage().removeItem(this._itemName(a.id));
            var b = a.id.toString();
            for (var c = 0, d; c < this.records.length; c++)
                this.records[c] === b && this.records.splice(c, 1);
            return this.save(), a
        },
        localStorage: function() {
            return localStorage
        },
        _clear: function() {
            var a = this.localStorage(), b = new RegExp("^" + this.name + "-");
            a.removeItem(this.name);
            for (var c in a)
                b.test(c) && a.removeItem(c);
            this.records.length = 0
        },
        _storageSize: function() {
            return this.localStorage().length
        },
        _itemName: function(a) {
            return this.name + "-" + a
        }
    }), a.LocalStorage.sync = window.Store.sync = a.localSync = function(b, c, d) {
        var e = c.localStorage || c.collection.localStorage, f, g, h = a.$ ? a.$.Deferred && a.$.Deferred(): a.Deferred && a.Deferred();
        try {
            switch (b) {
            case"read":
                f = c.id != undefined ? e.find(c) : e.findAll();
                break;
            case"create":
                f = e.create(c);
                break;
            case"update":
                f = e.update(c);
                break;
            case"delete":
                f = e.destroy(c)
            }
        } catch (i) {
            i.code === 22 && e._storageSize() === 0 ? g = "Private browsing is unsupported" : g = i.message
        }
        return f ? (d && d.success && (a.VERSION === "0.9.10" ? d.success(c, f, d) : d.success(f)), h && h.resolve(f)) : (g = g ? g : "Record Not Found", d && d.error && (a.VERSION === "0.9.10" ? d.error(c, g, d) : d.error(g)), h && h.reject(g)), d && d.complete && d.complete(f), h && h.promise()
    }, a.ajaxSync = a.sync, a.getSyncMethod = function(b) {
        return b.localStorage || b.collection && b.collection.localStorage ? a.localSync : a.ajaxSync
    }, a.sync = function(b, c, d) {
        return a.getSyncMethod(c).apply(this, [b, c, d])
    }, a.LocalStorage
});

