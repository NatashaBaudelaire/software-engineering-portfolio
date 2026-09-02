package ships;

public abstract class Ships {
    protected String name;
    protected int capacity;
    protected boolean loading;
    protected boolean loaded;
    protected boolean unloaded;

    public Ships(String name, int capacity) {
        this.name = name;
        this.capacity = capacity;
        this.loading = false;
        this.loaded = false;
        this.unloaded = false;
    }

    public void startLoading() {
        if (!loaded && !loading) {
            loading = true;
            unloaded = false;
        }
    }

    public void finishLoading() {
        if (loading) {
            loading = false;
            loaded = true;
        }
    }

    public void unload() {
        if (loaded) {
            loaded = false;
            unloaded = true;
        }
    }

    public boolean isLoaded() {
        return loaded;
    }

    public boolean isUnloaded() {
        return unloaded;
    }

    @Override
    public String toString() {
        return String.format("%s [Name: %s, Capacity: %d, Loading: %b, Loaded: %b, Unloaded: %b]",
                this.getClass().getSimpleName(), name, capacity, loading, loaded, unloaded);
    }
}
