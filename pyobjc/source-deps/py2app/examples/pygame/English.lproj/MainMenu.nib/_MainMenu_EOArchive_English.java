// _MainMenu_EOArchive_English.java
// Generated by EnterpriseObjects palette at Tuesday, March 2, 2004 8:45:51 PM America/New_York

import com.webobjects.eoapplication.*;
import com.webobjects.eocontrol.*;
import com.webobjects.eointerface.*;
import com.webobjects.eointerface.swing.*;
import com.webobjects.foundation.*;
import javax.swing.*;

public class _MainMenu_EOArchive_English extends com.webobjects.eoapplication.EOArchive {
    PygameAppDelegate _pygameAppDelegate0;

    public _MainMenu_EOArchive_English(Object owner, NSDisposableRegistry registry) {
        super(owner, registry);
    }

    protected void _construct() {
        Object owner = _owner();
        EOArchive._ObjectInstantiationDelegate delegate = (owner instanceof EOArchive._ObjectInstantiationDelegate) ? (EOArchive._ObjectInstantiationDelegate)owner : null;
        Object replacement;

        super._construct();


        if ((delegate != null) && ((replacement = delegate.objectForOutletPath(this, "delegate")) != null)) {
            _pygameAppDelegate0 = (replacement == EOArchive._ObjectInstantiationDelegate.NullObject) ? null : (PygameAppDelegate)replacement;
            _replacedObjects.setObjectForKey(replacement, "_pygameAppDelegate0");
        } else {
            _pygameAppDelegate0 = (PygameAppDelegate)_registered(new PygameAppDelegate(), "PygameAppDelegate");
        }
    }

    protected void _awaken() {
        super._awaken();
        .addActionListener((com.webobjects.eointerface.swing.EOControlActionAdapter)_registered(new com.webobjects.eointerface.swing.EOControlActionAdapter(_owner(), "unhideAllApplications", ), ""));
        .addActionListener((com.webobjects.eointerface.swing.EOControlActionAdapter)_registered(new com.webobjects.eointerface.swing.EOControlActionAdapter(_owner(), "hide", ), ""));
        .addActionListener((com.webobjects.eointerface.swing.EOControlActionAdapter)_registered(new com.webobjects.eointerface.swing.EOControlActionAdapter(_owner(), "hideOtherApplications", ), ""));
        .addActionListener((com.webobjects.eointerface.swing.EOControlActionAdapter)_registered(new com.webobjects.eointerface.swing.EOControlActionAdapter(_owner(), "orderFrontStandardAboutPanel", ), ""));

        if (_replacedObjects.objectForKey("_pygameAppDelegate0") == null) {
            _connect(_owner(), _pygameAppDelegate0, "delegate");
        }

        .addActionListener((com.webobjects.eointerface.swing.EOControlActionAdapter)_registered(new com.webobjects.eointerface.swing.EOControlActionAdapter(_owner(), "terminate", ), ""));
    }

    protected void _init() {
        super._init();
        .addActionListener((com.webobjects.eointerface.swing.EOControlActionAdapter)_registered(new com.webobjects.eointerface.swing.EOControlActionAdapter(null, "undo", ), ""));
        .addActionListener((com.webobjects.eointerface.swing.EOControlActionAdapter)_registered(new com.webobjects.eointerface.swing.EOControlActionAdapter(null, "paste", ), ""));
        .addActionListener((com.webobjects.eointerface.swing.EOControlActionAdapter)_registered(new com.webobjects.eointerface.swing.EOControlActionAdapter(null, "arrangeInFront", ), ""));
        .addActionListener((com.webobjects.eointerface.swing.EOControlActionAdapter)_registered(new com.webobjects.eointerface.swing.EOControlActionAdapter(null, "copy", ), ""));
        .addActionListener((com.webobjects.eointerface.swing.EOControlActionAdapter)_registered(new com.webobjects.eointerface.swing.EOControlActionAdapter(null, "showHelp", ), ""));
        .addActionListener((com.webobjects.eointerface.swing.EOControlActionAdapter)_registered(new com.webobjects.eointerface.swing.EOControlActionAdapter(null, "clearRecentDocuments", ), ""));
        .addActionListener((com.webobjects.eointerface.swing.EOControlActionAdapter)_registered(new com.webobjects.eointerface.swing.EOControlActionAdapter(null, "selectAll", ), ""));
        .addActionListener((com.webobjects.eointerface.swing.EOControlActionAdapter)_registered(new com.webobjects.eointerface.swing.EOControlActionAdapter(null, "performMiniaturize", ), ""));
        .addActionListener((com.webobjects.eointerface.swing.EOControlActionAdapter)_registered(new com.webobjects.eointerface.swing.EOControlActionAdapter(null, "toggleContinuousSpellChecking", ), ""));
        .addActionListener((com.webobjects.eointerface.swing.EOControlActionAdapter)_registered(new com.webobjects.eointerface.swing.EOControlActionAdapter(null, "print", ), ""));
        .addActionListener((com.webobjects.eointerface.swing.EOControlActionAdapter)_registered(new com.webobjects.eointerface.swing.EOControlActionAdapter(null, "cut", ), ""));
        .addActionListener((com.webobjects.eointerface.swing.EOControlActionAdapter)_registered(new com.webobjects.eointerface.swing.EOControlActionAdapter(null, "runPageLayout", ), ""));
        .addActionListener((com.webobjects.eointerface.swing.EOControlActionAdapter)_registered(new com.webobjects.eointerface.swing.EOControlActionAdapter(null, "checkSpelling", ), ""));
        .addActionListener((com.webobjects.eointerface.swing.EOControlActionAdapter)_registered(new com.webobjects.eointerface.swing.EOControlActionAdapter(null, "delete", ), ""));
        .addActionListener((com.webobjects.eointerface.swing.EOControlActionAdapter)_registered(new com.webobjects.eointerface.swing.EOControlActionAdapter(null, "redo", ), ""));
        .addActionListener((com.webobjects.eointerface.swing.EOControlActionAdapter)_registered(new com.webobjects.eointerface.swing.EOControlActionAdapter(null, "performClose", ), ""));
        .addActionListener((com.webobjects.eointerface.swing.EOControlActionAdapter)_registered(new com.webobjects.eointerface.swing.EOControlActionAdapter(null, "showGuessPanel", ), ""));
    }
}
